import re
import requests
import hashlib

def check_password_strength(password):
    score = 0
    feedback = []  # This line should be here to define the feedback list

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password is too short. Use at least 12 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add uppercase letters for a stronger password.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Add lowercase letters for better security.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Add numbers to increase password strength.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("⚠️ Add special characters for better security.")

    # Check if password is common
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
    if password in common_passwords:
        score = 0  # Reset score if password is too common
        feedback.append("❌ This password is too common! Choose something unique.")

    # Strength rating
    if score >= 5:
        strength = "✅ Strong Password"
    elif 3 <= score < 5:
        strength = "⚠️ Medium Strength Password"
    else:
        strength = "❌ Weak Password"

    return strength, feedback

# Optional: Check if password has been breached
def check_breach(password):
    sha1_pass = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_pass[:5], sha1_pass[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if suffix in response.text:
        return "❌ Your password has been breached! Choose a new one."
    else:
        return "✅ This password has not been found in data breaches."

# Example usage
password = input("Enter a password to check: ")
strength, feedback = check_password_strength(password)
print("\nPassword Strength:", strength)
for suggestion in feedback:
    print(suggestion)

# Uncomment to check password breach
# print(check_breach(password))
