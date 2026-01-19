import re

UNIT_PATTERN = r"(M/uL|g/dL|mg/dL|/uL|mmol/L|%)"

def extract_candidate_tests(tests_raw):
    candidates = []

    for line in tests_raw:
        has_number = bool(re.search(r"\d", line))
        has_unit = bool(re.search(UNIT_PATTERN, line, re.IGNORECASE))

        if has_number and has_unit:
            cleaned = line.replace("CBC:", "").strip()
            candidates.append(cleaned)

    return candidates
