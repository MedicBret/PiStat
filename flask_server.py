from flask import Flask, render_template_string, request
import json
import os
import logging
from profiles import profiles

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SELECTION_FILE = os.path.join(BASE_DIR, "selection.json")
SCANNED_FLAG = os.path.join(BASE_DIR, "scanned.flag")

app = Flask(__name__)

def get_profile_options():
    options = '<option value="" disabled selected>--Select Profile--</option>\n'
    for profile in profiles.keys():
        options += f'<option value="{profile}">{profile}</option>\n'
    return options

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>PiStat Control Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        h2 { font-size: 2em; }
        select, input[type=submit] {
            font-size: 1.2em;
            padding: 8px;
            margin: 10px;
        }
        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 90%%;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px 12px;
            text-align: left;
        }
        th {
            background-color: #eee;
        }
        .result-container {
            display: flex;
            justify-content: center;
            gap: 50px;
            flex-wrap: wrap;
        }
    </style>
</head>
<body>
    <img src="/static/logo.png" alt="SIM iSTAT Logo" width="180"><br>
    <h2>PiStat Control Panel</h2>
    <form method="post">
        <label><strong>Profile:</strong></label>
        <select name="profile">
            {{ profile_options|safe }}
        </select>
        <label><strong>Severity:</strong></label>
        <select name="severity" required>
            <option value="" disabled selected>--Set Severity--</option>
            <option value="mild">Mild</option>
            <option value="moderate">Moderate</option>
            <option value="critical">Critical</option>
        </select>

        <input type="submit" value="Set">
    </form>

    {% if result %}
    <div class="result-container">
        <div>
            <h3>CHEM8+</h3>
            <table>
                {% for key, value in result["CHEM8+"].items() %}
                <tr><td><strong>{{ key }}</strong></td><td>{{ value }}</td></tr>
                {% endfor %}
            </table>
        </div>
        <div>
            <h3>CG4+</h3>
            <table>
                {% for key, value in result["CG4+"].items() %}
                <tr><td><strong>{{ key }}</strong></td><td>{{ value }}</td></tr>
                {% endfor %}
            </table>
        </div>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def control():
    profile = "None"
    severity = "None"
    result = None

    if request.method == 'POST':
        profile = request.form.get('profile', 'None')
        severity = request.form.get('severity', 'None')
        try:
            # Write the selection file
            with open(SELECTION_FILE, "w") as f:
                json.dump({"profile": profile, "severity": severity}, f)
            # Create the scanned flag file
            with open(SCANNED_FLAG, "w") as f:
                f.write("scanned")
            logging.info("scanned.flag written successfully")
        except Exception as e:
            logging.error("Error writing files: %s", e)

        if profile in profiles and severity in profiles[profile]:
            result = profiles[profile][severity]

    return render_template_string(
        HTML,
        profile=profile,
        severity=severity,
        profile_options=get_profile_options(),
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
