# Dictionaries for conditions and vaccine history
CONDITIONS = {
    "lung": "Chronic lung disease",
    "liver": "Chronic liver disease",
    "heart": "Heart failure",
    "diabetes": "Diabetes",
    "immune": "Immunocompromised",
}

VACCINES = {
    "pcv20": "PCV20",
    "pcv15": "PCV15",
    "ppsv23": "PPSV23"
}

def get_age():
    return int(input("Age: "))

def get_conditions():
    cond = {}
    for key, label in CONDITIONS.items():
        cond[key] = input(f"{label} (yes/no): ").lower() == "yes"
    return cond

def get_history():
    hist = {}
    for key, label in VACCINES.items():
        hist[key] = input(f"{label} received (yes/no): ").lower() == "yes"
    return hist

def eligible(age, cond):
    if age >= 50:
        return True
    if 19 <= age <= 49 and any(cond.values()):
        return True
    return False

def recommend(eligible, hist):
    if not eligible:
        return "Not eligible."
    if hist["pcv20"]:
        return "Complete."
    if hist["pcv15"] and not hist["ppsv23"]:
        return "Give PPSV23."
    if not any(hist.values()):
        return "Give PCV20."
    if hist["ppsv23"] and not hist["pcv15"]:
        return "Give PCV20."
    return "Complete."

def main():
    age = get_age()
    cond = get_conditions()
    hist = get_history()
    print(recommend(eligible(age, cond), hist))

main()


