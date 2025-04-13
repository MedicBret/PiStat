import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import json
import subprocess
import logging
from profiles import profiles

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Define base directory and file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SELECTION_FILE = os.path.join(BASE_DIR, "selection.json")
HISTORY_FILE = os.path.join(BASE_DIR, "results_history.json")
SCANNED_FLAG = os.path.join(BASE_DIR, "scanned.flag")
MAX_HISTORY = 10

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            logging.error("Error loading history: %s", e)
            return []
    return []

def save_history(history):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history[-MAX_HISTORY:], f)
    except Exception as e:
        logging.error("Error saving history: %s", e)

normal_ranges = {
    "Na": (135, 145), "K": (3.5, 5.0), "Cl": (98, 107), "BUN": (7, 20),
    "Glu": (70, 110), "Crea": (0.6, 1.3), "iCa": (1.1, 1.3), "TCO2": (22, 29),
    "Hct": (36, 50), "Angap": (8, 16), "Hb": (12, 18),
    "pH": (7.35, 7.45), "PCO2": (35, 45), "PO2": (80, 100), "HCO3": (22, 26),
    "BE": (-2, 2), "sO2": (95, 100), "Lactate": (0.5, 2.0)
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PiStat")
        self.attributes("-fullscreen", True)
        self.configure(bg="white")
        self.bind("<Escape>", lambda e: self.return_to_desktop())
        self.container = tk.Frame(self, bg="white")
        self.container.pack(fill="both", expand=True)
        self.frames = {}
        for F in (BootScreen, SelectTestScreen, ProgressScreen, StudentDisplayScreen, ResultsScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)
        self.selected_test = None
        self.result = None
        self.show_frame(BootScreen)
        # Remove scanned flag on startup if it exists
        if os.path.exists(SCANNED_FLAG):
            try:
                os.remove(SCANNED_FLAG)
            except Exception as e:
                logging.error("Error removing scanned flag: %s", e)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        if frame_class == ProgressScreen:
            frame.start_test()
        elif frame_class == StudentDisplayScreen:
            frame.set_result(self.result)
        elif frame_class == ResultsScreen:
            frame.update_results()
        frame.tkraise()

    def return_to_desktop(self):
        self.destroy()
        subprocess.Popen(["lxsession"])

class BootScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.bind("<Escape>", lambda e: controller.return_to_desktop())
        try:
            logo_path = os.path.join(BASE_DIR, "static", "logo.png")
            img = Image.open(logo_path)
            img = img.resize((120, 120), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(self, image=self.logo, bg="white").pack(pady=10)
        except Exception as e:
            logging.warning("Could not load logo: %s", e)
            tk.Label(self, text="Logo", font=("Helvetica", 24), bg="white").pack(pady=10)

        tk.Label(
            self,
            text="YOU, More Prepared Than Ever",
            font=("Helvetica", 20),
            fg="red",
            bg="white",
            wraplength=300,
            justify="center"
        ).pack(pady=5)

        self.after(5000, lambda: controller.show_frame(SelectTestScreen))

class SelectTestScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.bind("<Escape>", lambda e: controller.return_to_desktop())
        tk.Label(self, text="Select Test", font=("Helvetica", 24), bg="white").pack(pady=15)
        tk.Button(self, text="CHEM8+", font=("Helvetica", 18), command=lambda: self.select_test("CHEM8+")).pack(pady=8)
        tk.Button(self, text="CG4+", font=("Helvetica", 18), command=lambda: self.select_test("CG4+")).pack(pady=8)
        tk.Button(self, text="Results", font=("Helvetica", 18), command=lambda: controller.show_frame(ResultsScreen)).pack(pady=8)

    def select_test(self, test_type):
        self.controller.selected_test = test_type
        self.controller.show_frame(ProgressScreen)

class ProgressScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.bind("<Escape>", lambda e: controller.return_to_desktop())
        tk.Label(self, text="Running PiStat Test...", font=("Helvetica", 20), bg="white").pack(pady=20)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(pady=20)
        self.progress["maximum"] = 100
        self.current_progress = 0
        self.after_id = None

    def start_test(self):
        self.current_progress = 0
        self.progress["value"] = 0
        if self.after_id:
            self.after_cancel(self.after_id)
        self.update_progress()

    def update_progress(self):
        increment = 100 / 240  # total duration ~120 seconds (0.5 sec interval)
        self.current_progress += increment
        self.progress["value"] = self.current_progress
        if self.current_progress < 100:
            self.after_id = self.after(500, self.update_progress)
        else:
            self.complete_test()

    def complete_test(self):
        try:
            with open(SELECTION_FILE) as f:
                data = json.load(f)
            profile = data.get("profile")
            severity = data.get("severity")
            test = self.controller.selected_test
            if profile in profiles and severity in profiles[profile] and test in profiles[profile][severity]:
                result = profiles[profile][severity][test]
                self.controller.result = result
                history = load_history()
                history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "test": test,
                    "result": result
                })
                save_history(history)
            else:
                self.controller.result = {"Error": "No valid selection found"}
        except Exception as e:
            logging.error("Error completing test: %s", e)
            self.controller.result = {"Error": "Test completion error"}
        self.controller.show_frame(StudentDisplayScreen)

class StudentDisplayScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.bind("<Escape>", lambda e: controller.return_to_desktop())
        self.header = tk.Label(self, text="", font=("Courier", 18), bg="white")
        self.header.pack(pady=5)
        self.test_label = tk.Label(self, text="", font=("Helvetica", 20, "bold"), bg="white")
        self.test_label.pack(pady=5)
        self.result_frame = tk.Frame(self, bg="white")
        self.result_frame.pack()
        tk.Button(self, text="Back", font=("Helvetica", 16), command=lambda: controller.show_frame(SelectTestScreen)).pack(pady=15)

    def set_result(self, result):
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        now = datetime.now()
        self.header.config(text=now.strftime("%H:%M  %d%b%y").upper())
        test_label = self.controller.selected_test or "PiStat"
        self.test_label.config(text=f"PiStat {test_label}")
        if result:
            for key, value in result.items():
                try:
                    numeric_value = float(value)
                    color = "red" if key in normal_ranges and not (normal_ranges[key][0] <= numeric_value <= normal_ranges[key][1]) else "black"
                except ValueError:
                    color = "black"
                tk.Label(self.result_frame, text=f"{key}: {value}", font=("Courier", 16), fg=color, bg="white").pack()

class ResultsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.bind("<Escape>", lambda e: controller.return_to_desktop())
        tk.Label(self, text="Recent Results", font=("Helvetica", 24, "bold"), bg="white").pack(pady=10)

        self.canvas = tk.Canvas(self, bg="white")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        # Update the scrollregion when the scrollable frame's size changes.
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Back button now returns to the student display screen.
        tk.Button(self, text="Back", font=("Helvetica", 16),
                  command=lambda: controller.show_frame(StudentDisplayScreen)).pack(pady=10)

        # Bind mouse wheel scrolling when the cursor is over the canvas.
        self.canvas.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        self.canvas.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

    def _on_mousewheel(self, event):
        # On Windows, event.delta is typically a multiple of 120.
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def update_results(self):
        # Clear previous results.
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        history = load_history()
        if not history:
            tk.Label(self.scrollable_frame, text="No results available.", font=("Helvetica", 18), bg="white").pack()
        else:
            for entry in reversed(history):
                timestamp = entry.get("timestamp", "Unknown")
                result = entry.get("result", {})
                tk.Label(self.scrollable_frame, text=f"{timestamp}", font=("Helvetica", 16, "bold"), bg="white").pack(pady=(10, 0))
                for key, value in result.items():
                    try:
                        numeric_value = float(value)
                        color = "red" if key in normal_ranges and not (normal_ranges[key][0] <= numeric_value <= normal_ranges[key][1]) else "black"
                    except ValueError:
                        color = "black"
                    tk.Label(self.scrollable_frame, text=f"{key}: {value}", font=("Courier", 16), fg=color, bg="white").pack(anchor="w", padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()
