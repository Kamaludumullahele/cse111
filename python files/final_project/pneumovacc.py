
import csv
from datetime import date, datetime, timedelta

conditions = {
        1: "diabetes",
        2: "chronic_lung_disease",
        3: "copd",
        4: "asthma_severe",
        5: "chronic_heart_disease",
        6: "chronic_kidney_disease",
        7: "chronic_liver_disease",
        8: "immunocompromised",
        9: "smoker",
        10: "homelessness",
        11: "cochlear_implant",
        12: "csf_leak",
}

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year
    age = 0 if age < 0 else age  # Ensure age is not negative
    # Cap age at 150 to avoid unrealistic values
    age = min(age, 115) 
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def eligibility(age, selected_keys):
    if age >= 65:
        return True

    # Check if any of the selected conditions are in the predefined conditions
    return any(k in conditions for k in selected_keys)


def main():
    while True:
        dob_str = input("Enter your date of birth (YYYY-MM-DD): ").strip()
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue  # restart from beginning

        age = calculate_age(dob)
        print(f"You are {age} years old.")

        if age >= 65:
            print("You are eligible for vaccination based on age.")
            break  # valid end

        condition_input = input("Do you have any of the listed conditions? (yes/no): ").strip().lower()
        if condition_input in ("yes", "y"):
            print("Enter condition key(s), comma-separated. Example: 1,4,9")
            for k, v in conditions.items():
                print(f"{k}: {v}")

            raw = input("Keys: ").strip()
            try:
                selected_keys = [int(x.strip()) for x in raw.split(",") if x.strip()]
            except ValueError:
                print("Invalid key format. Use numbers like: 1,4,9")
                continue  # restart from beginning

            invalid = [k for k in selected_keys if k not in conditions]
            if invalid:
                print(f"Invalid key(s): {invalid}")
                continue  # restart from beginning

            if eligibility(age, selected_keys):
                print("You are eligible for vaccination.")
            else:
                print("You are not eligible for vaccination.")
            break  # valid end

        elif condition_input in ("no", "n"):
            print("You are not eligible for vaccination.")
            break  # valid end

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue  # restart from beginning

if __name__ == "__main__":
    main()
