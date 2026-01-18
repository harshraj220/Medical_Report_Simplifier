REFERENCE_RANGES = {
    "Hemoglobin": {
        "unit": "g/dL",
        "low": 12.0,
        "high": 15.0
    },
    "WBC": {
        "unit": "/uL",
        "low": 4000,
        "high": 11000
    }
}

def normalize_test(test):
    name = test["name"]

    if name not in REFERENCE_RANGES:
        return None

    ref = REFERENCE_RANGES[name]

    if test["unit"] != ref["unit"]:
        return None

    value = test["value"]

    if value < ref["low"]:
        status = "low"
    elif value > ref["high"]:
        status = "high"
    else:
        status = "normal"

    return {
        "name": name,
        "value": value,
        "unit": test["unit"],
        "status": status,
        "ref_range": {
            "low": ref["low"],
            "high": ref["high"]
        }
    }
