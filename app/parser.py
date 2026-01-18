import re

UNIT_PATTERN = r"(g/dL|mg/dL|/uL|mmol/L|%)"
STATUS_PATTERN = r"\((Low|High|Normal)\)"

def parse_test_line(line: str):
    value_match = re.search(r"(\d+\.?\d*)", line)
    if not value_match:
        return None

    value = float(value_match.group(1))

    unit_match = re.search(UNIT_PATTERN, line, re.IGNORECASE)
    if not unit_match:
        return None

    unit = unit_match.group(1)

    status_match = re.search(STATUS_PATTERN, line, re.IGNORECASE)
    status = status_match.group(1).lower() if status_match else "unknown"

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
