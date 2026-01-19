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

        elif name == "Platelets":
            if status == "normal":
                summaries.append("Platelet count is normal.")
                explanations.append(
                    "Platelets differ from other blood cells; they help your blood clot to stop bleeding."
                )
            elif status == "low":
                summaries.append("Platelet count is lower than normal.")
                explanations.append(
                    "Low platelet count (thrombocytopenia) may increase the risk of bleeding or bruising."
                )
            elif status == "high":
                summaries.append("Platelet count is higher than normal.")
                explanations.append(
                    "High platelet count (thrombocytosis) can occur with inflammation or infection."
                )

        elif name == "RBC":
            if status == "normal":
                summaries.append("Red blood cell count is normal.")
                explanations.append(
                    "Red blood cells carry oxygen from your lungs to the rest of your body."
                )
            elif status == "low":
                summaries.append("Red blood cell count is low.")
                explanations.append(
                    "A low red blood cell count typically indicates anemia."
                )
            elif status == "high":
                summaries.append("Red blood cell count is high.")
                explanations.append(
                    "A high red blood cell count may be caused by dehydration or lung issues."
                )

        elif name == "Glucose":
            if status == "normal":
                summaries.append("Blood glucose level is normal.")
                explanations.append(
                    "Glucose is the main source of energy for your body's cells."
                )
            elif status == "high":
                summaries.append("Blood glucose level is higher than normal.")
                explanations.append(
                    "High glucose levels can be a sign of pre-diabetes or diabetes."
                )
            elif status == "low":
                summaries.append("Blood glucose level is lower than normal.")
                explanations.append(
                    "Low glucose levels (hypoglycemia) can cause shakiness or confusion."
                )

        elif name == "Creatinine":
            if status == "normal":
                summaries.append("Creatinine level is normal.")
                explanations.append(
                    "Creatinine is a waste product filtered by your kidneys."
                )
            elif status == "high":
                summaries.append("Creatinine level is high.")
                explanations.append(
                    "High creatinine levels may indicate that your kidneys are not working optimally."
                )
            elif status == "low":
                summaries.append("Creatinine level is low.")
                explanations.append(
                    "Low creatinine levels are generally not concerning but can improve with muscle mass."
                )

    return {
        "summary": " ".join(summaries),
        "explanations": explanations
    }
