def explain_tests(tests):
    summaries = []
    explanations = []

    for test in tests:
        name = test["name"]
        status = test["status"]

        if name == "WBC":
            if status == "normal":
                summaries.append("White blood cell count is within the normal range.")
                explanations.append(
                    "A normal white blood cell count generally suggests no active infection."
                )
            elif status == "high":
                summaries.append("White blood cell count is higher than normal.")
                explanations.append(
                    "A high white blood cell count can occur with infections or inflammation."
                )
            elif status == "low":
                summaries.append("White blood cell count is lower than normal.")
                explanations.append(
                    "A low white blood cell count may reduce the body's ability to fight infections."
                )

        elif name == "Hemoglobin":
            if status == "normal":
                summaries.append("Hemoglobin level is within the normal range.")
                explanations.append(
                    "Normal hemoglobin levels indicate adequate oxygen-carrying capacity in the blood."
                )
            elif status == "low":
                summaries.append("Hemoglobin level is lower than normal.")
                explanations.append(
                    "Low hemoglobin levels may be associated with anemia."
                )
            elif status == "high":
                summaries.append("Hemoglobin level is higher than normal.")
                explanations.append(
                    "High hemoglobin levels can occur due to dehydration or other conditions."
                )

    return {
        "summary": " ".join(summaries),
        "explanations": explanations
    }
