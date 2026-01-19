import re

UNIT_PATTERN = r"(M/uL|g/dL|mg/dL|/uL|mmol/L|%)"
STATUS_PATTERN = r"\((Low|High|Normal)\)"

def parse_test_line(line: str):
    # 1. Find the unit first (crucial to anchor the value)
    unit_match = re.search(UNIT_PATTERN, line, re.IGNORECASE)
    if not unit_match:
        return None

    unit = unit_match.group(1)
    
    # 2. Look for the status (Low/High/Normal)
    status_match = re.search(STATUS_PATTERN, line, re.IGNORECASE)
    status = status_match.group(1).lower() if status_match else "unknown"

    # 3. Find the value immediately *before* the unit
    # Everything before the unit is candidate text
    unit_start = unit_match.start()
    pre_unit_text = line[:unit_start]

    # Find all number candidates in the text before the unit
    # We take the *last* number found, assuming "Name Value Unit" format
    # This fixes issues like "Vitamin B12 100 mg/dL" where "12" was previously matched
    number_matches = list(re.finditer(r"(\d+\.?\d*)", pre_unit_text))
    
    if not number_matches:
        return None
        
    value_match = number_matches[-1]
    value = float(value_match.group(1))

    # 4. Extract name (everything before the value)
    name_part = line[:value_match.start()].strip()
    name = name_part.replace(":", "").strip()

    if not name:
        return None

    return {
        "name": name,
        "value": value,
        "unit": unit,
        "status": status
    }
