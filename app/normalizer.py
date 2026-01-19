REFERENCE_RANGES = {
    "Hemoglobin": {
        "unit": "g/dL",
        "low": 12.0,
        "high": 17.0,
        "aliases": ["Hb", "Hgb", "Hemaglobin"]
    },
    "WBC": {
        "unit": "/uL",
        "low": 4000,
        "high": 11000,
        "aliases": ["White Blood Cell", "W.B.C.", "Leukocytes", "WBC Count"]
    },
    "Platelets": {
        "unit": "/uL",
        "low": 150000,
        "high": 450000,
        "aliases": ["Plt", "Platelet Count", "Thrombocytes"]
    },
    "RBC": {
        "unit": "M/uL",
        "low": 4.0,
        "high": 6.1,
        "aliases": ["Red Blood Cell", "R.B.C.", "Erythrocytes", "RBC Count"]
    },
    "Glucose": {
        "unit": "mg/dL",
        "low": 70,
        "high": 100,
        "aliases": ["Fasting Blood Sugar", "FBS", "Sugar", "Blood Glucose"]
    },
    "Creatinine": {
        "unit": "mg/dL",
        "low": 0.6,
        "high": 1.2,
        "aliases": ["Serum Creatinine", "Creat"]
    }
}

def get_normalized_name(raw_name: str):
    """
    Tries to map a raw test name to a canonical test name using case-insensitive matching
    against the keys and aliases in REFERENCE_RANGES.
    """
    raw_lower = raw_name.lower()
    
    # Check direct keys
    for key in REFERENCE_RANGES:
        if key.lower() == raw_lower:
            return key
            
    # Check aliases
    for key, data in REFERENCE_RANGES.items():
        aliases = [a.lower() for a in data.get("aliases", [])]
        if raw_lower in aliases:
            return key
            
    return None

def normalize_test(test):
    # Try to resolve the name to a canonical one
    canonical_name = get_normalized_name(test["name"])

    if not canonical_name:
        return None

    ref = REFERENCE_RANGES[canonical_name]

    # Validate unit (simple exact match for now)
    if test["unit"] != ref["unit"]:
        # Handle simple variation like uL vs /uL if needed, or strict for now
        return None

    value = test["value"]

    if value < ref["low"]:
        status = "low"
    elif value > ref["high"]:
        status = "high"
    else:
        status = "normal"

    return {
        "name": canonical_name,
        "value": value,
        "unit": ref["unit"],
        "status": status,
        "ref_range": {
            "low": ref["low"],
            "high": ref["high"]
        }
    }
