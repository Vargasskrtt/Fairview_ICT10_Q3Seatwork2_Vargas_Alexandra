import random

# List of possible teams
teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

# Ask the user for inputs
registration = input("Confirmation of Intramurals online registration (yes/no): ").strip().lower()
medical = input("Confirmation of medical clearance (yes/no): ").strip().lower()
grade_input = input("Grade level (7-11): ").strip()
section = input("Section (Emerald, Ruby, Sapphire, Opaz, Jade): ").strip()

# Convert grade to integer if possible
grade = int(grade_input) if grade_input.isdigit() else None

# Eligibility logic
if registration == "yes":
    if medical == "yes":
        if grade is not None and 7 <= grade <= 10:
            team = random.choice(teams)
            print("🎉 Congratulations! You are eligible to join the Intramurals.")
            print(f"Team: {team}")
            print(f"Section: {section}")
        else:
            print("❌ Only students in Grades 7–10 are eligible.")
    else:
        print("❌ You must secure a medical clearance to join the Intramurals.")
else:
    print("❌ You must register online to join the Intramurals.")
