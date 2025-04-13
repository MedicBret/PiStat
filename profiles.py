# profiles.py
# Contains predefined profiles and their corresponding test values for the PiStat application.

profiles = {
    "Trauma": {
        "mild": {
            "CHEM8+": {
                "Na": 140, "K": 4.0, "Cl": 100, "iCa": 1.2, "Glu": 90,
                "BUN": 15, "Crea": 1.0, "Hct": 40, "TCO2": 25.4
            },
            "CG4+": {
                "pH": 7.35, "PCO2": 40, "PO2": 95, "TCO2": 25.4,
                "HCO3": 24, "BE": 0, "sO2": 98
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 138, "K": 4.5, "Cl": 102, "iCa": 1.15, "Glu": 100,
                "BUN": 18, "Crea": 1.2, "Hct": 38, "TCO2": 23.6
            },
            "CG4+": {
                "pH": 7.30, "PCO2": 45, "PO2": 85, "TCO2": 23.6,
                "HCO3": 22, "BE": -2, "sO2": 96
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 134, "K": 5.2, "Cl": 105, "iCa": 1.05, "Glu": 120,
                "BUN": 22, "Crea": 1.4, "Hct": 35, "TCO2": 19.0
            },
            "CG4+": {
                "pH": 7.10, "PCO2": 55, "PO2": 60, "TCO2": 19.0,
                "HCO3": 18, "BE": -6, "sO2": 92
            }
        }
    },
    "DKA": {
        "mild": {
            "CHEM8+": {
                "Na": 138, "K": 5.0, "Cl": 100, "iCa": 1.2, "Glu": 250,
                "BUN": 20, "Crea": 1.2, "Hct": 42, "TCO2": 19.3
            },
            "CG4+": {
                "pH": 7.30, "PCO2": 35, "PO2": 95, "TCO2": 19.3,
                "HCO3": 18, "BE": -5, "sO2": 97
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 135, "K": 5.5, "Cl": 102, "iCa": 1.15, "Glu": 450,
                "BUN": 26, "Crea": 1.6, "Hct": 44, "TCO2": 15.1
            },
            "CG4+": {
                "pH": 7.20, "PCO2": 30, "PO2": 90, "TCO2": 15.1,
                "HCO3": 14, "BE": -8, "sO2": 95
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 130, "K": 6.0, "Cl": 105, "iCa": 1.05, "Glu": 650,
                "BUN": 35, "Crea": 2.0, "Hct": 46, "TCO2": 10.8
            },
            "CG4+": {
                "pH": 6.90, "PCO2": 20, "PO2": 80, "TCO2": 10.8,
                "HCO3": 8, "BE": -15, "sO2": 90
            }
        }
    },
    "TBI": {
        "mild": {
            "CHEM8+": {
                "Na": 140, "K": 4.1, "Cl": 101, "iCa": 1.2, "Glu": 85,
                "BUN": 14, "Crea": 1.0, "Hct": 39, "TCO2": 25.4
            },
            "CG4+": {
                "pH": 7.38, "PCO2": 38, "PO2": 90, "TCO2": 25.4,
                "HCO3": 24, "BE": 1, "sO2": 97
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 138, "K": 4.5, "Cl": 102, "iCa": 1.1, "Glu": 110,
                "BUN": 18, "Crea": 1.3, "Hct": 38, "TCO2": 22.7
            },
            "CG4+": {
                "pH": 7.30, "PCO2": 45, "PO2": 80, "TCO2": 22.7,
                "HCO3": 20, "BE": -3, "sO2": 95
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 136, "K": 5.3, "Cl": 104, "iCa": 1.0, "Glu": 140,
                "BUN": 22, "Crea": 1.6, "Hct": 36, "TCO2": 17.6
            },
            "CG4+": {
                "pH": 7.15, "PCO2": 55, "PO2": 65, "TCO2": 17.6,
                "HCO3": 16, "BE": -7, "sO2": 91
            }
        }
    },
    "Sepsis": {
        "mild": {
            "CHEM8+": {
                "Na": 138, "K": 4.2, "Cl": 101, "iCa": 1.18, "Glu": 105,
                "BUN": 18, "Crea": 1.2, "Hct": 40, "TCO2": 22.4
            },
            "CG4+": {
                "pH": 7.36, "PCO2": 39, "PO2": 95, "TCO2": 22.4,
                "HCO3": 22, "BE": -1, "sO2": 97
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 136, "K": 4.8, "Cl": 102, "iCa": 1.12, "Glu": 130,
                "BUN": 22, "Crea": 1.5, "Hct": 38, "TCO2": 20.3
            },
            "CG4+": {
                "pH": 7.28, "PCO2": 44, "PO2": 85, "TCO2": 20.3,
                "HCO3": 18, "BE": -4, "sO2": 95
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 132, "K": 5.5, "Cl": 105, "iCa": 1.00, "Glu": 170,
                "BUN": 28, "Crea": 1.8, "Hct": 36, "TCO2": 15.5
            },
            "CG4+": {
                "pH": 7.10, "PCO2": 50, "PO2": 70, "TCO2": 15.5,
                "HCO3": 14, "BE": -8, "sO2": 90
            }
        }
    },
    "ARDS": {
        "mild": {
            "CHEM8+": {
                "Na": 138, "K": 4.0, "Cl": 100, "iCa": 1.18, "Glu": 95,
                "BUN": 17, "Crea": 1.1, "Hct": 41, "TCO2": 25.1
            },
            "CG4+": {
                "pH": 7.36, "PCO2": 38, "PO2": 80, "TCO2": 25.1,
                "HCO3": 24, "BE": 0, "sO2": 96
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 136, "K": 4.4, "Cl": 101, "iCa": 1.1, "Glu": 120,
                "BUN": 20, "Crea": 1.4, "Hct": 39, "TCO2": 21.2
            },
            "CG4+": {
                "pH": 7.28, "PCO2": 46, "PO2": 70, "TCO2": 21.2,
                "HCO3": 20, "BE": -3, "sO2": 94
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 134, "K": 5.1, "Cl": 104, "iCa": 1.05, "Glu": 135,
                "BUN": 24, "Crea": 1.7, "Hct": 37, "TCO2": 16.6
            },
            "CG4+": {
                "pH": 7.18, "PCO2": 55, "PO2": 60, "TCO2": 16.6,
                "HCO3": 16, "BE": -7, "sO2": 90
            }
        }
    },
    "DIC": {
        "mild": {
            "CHEM8+": {
                "Na": 137, "K": 4.0, "Cl": 100, "iCa": 1.2, "Glu": 100,
                "BUN": 18, "Crea": 1.1, "Hct": 40, "TCO2": 22.4
            },
            "CG4+": {
                "pH": 7.35, "PCO2": 40, "PO2": 90, "TCO2": 22.4,
                "HCO3": 22, "BE": -1, "sO2": 96
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 134, "K": 4.7, "Cl": 102, "iCa": 1.08, "Glu": 115,
                "BUN": 23, "Crea": 1.5, "Hct": 38, "TCO2": 20.6
            },
            "CG4+": {
                "pH": 7.26, "PCO2": 48, "PO2": 75, "TCO2": 20.6,
                "HCO3": 18, "BE": -5, "sO2": 94
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 130, "K": 5.5, "Cl": 104, "iCa": 0.98, "Glu": 145,
                "BUN": 30, "Crea": 2.0, "Hct": 36, "TCO2": 13.3
            },
            "CG4+": {
                "pH": 7.08, "PCO2": 55, "PO2": 60, "TCO2": 13.3,
                "HCO3": 12, "BE": -10, "sO2": 89
            }
        }
    },
    "Crush Injury": {
        "mild": {
            "CHEM8+": {
                "Na": 139, "K": 4.6, "Cl": 101, "iCa": 1.16, "Glu": 98,
                "BUN": 19, "Crea": 1.2, "Hct": 40, "TCO2": 22.8
            },
            "CG4+": {
                "pH": 7.32, "PCO2": 42, "PO2": 92, "TCO2": 22.8,
                "HCO3": 21, "BE": -2, "sO2": 96
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 137, "K": 5.3, "Cl": 103, "iCa": 1.05, "Glu": 115,
                "BUN": 25, "Crea": 1.6, "Hct": 38, "TCO2": 19.6
            },
            "CG4+": {
                "pH": 7.25, "PCO2": 47, "PO2": 82, "TCO2": 19.6,
                "HCO3": 18, "BE": -5, "sO2": 93
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 133, "K": 6.5, "Cl": 105, "iCa": 0.95, "Glu": 140,
                "BUN": 32, "Crea": 2.1, "Hct": 36, "TCO2": 15.4
            },
            "CG4+": {
                "pH": 7.10, "PCO2": 52, "PO2": 70, "TCO2": 15.4,
                "HCO3": 14, "BE": -8, "sO2": 91
            }
        }
    },
    "Crush Syndrome": {
        "mild": {
            "CHEM8+": {
                "Na": 138, "K": 5.2, "Cl": 101, "iCa": 1.1, "Glu": 105,
                "BUN": 20, "Crea": 1.3, "Hct": 40, "TCO2": 21.3
            },
            "CG4+": {
                "pH": 7.30, "PCO2": 44, "PO2": 90, "TCO2": 21.3,
                "HCO3": 20, "BE": -3, "sO2": 94
            }
        },
        "moderate": {
            "CHEM8+": {
                "Na": 135, "K": 6.0, "Cl": 104, "iCa": 1.0, "Glu": 130,
                "BUN": 26, "Crea": 1.8, "Hct": 38, "TCO2": 17.7
            },
            "CG4+": {
                "pH": 7.18, "PCO2": 50, "PO2": 75, "TCO2": 17.7,
                "HCO3": 16, "BE": -7, "sO2": 92
            }
        },
        "critical": {
            "CHEM8+": {
                "Na": 130, "K": 7.2, "Cl": 106, "iCa": 0.85, "Glu": 160,
                "BUN": 34, "Crea": 2.4, "Hct": 36, "TCO2": 11.7
            },
            "CG4+": {
                "pH": 7.05, "PCO2": 58, "PO2": 65, "TCO2": 11.7,
                "HCO3": 10, "BE": -12, "sO2": 89
            }
        }
    }
}
