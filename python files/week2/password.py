
import re


LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]
FILES = ["wordlist.txt", "toppasswords.txt"]
strength = -1
min_length = 10
strong_length = 16


def main():
    while True:
        password = input("Type a password to check its strength (or q to quit): ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        print(f"The entered password is: {password}")

        found = False
        for filename in FILES:
            if word_in_file(password, filename):
                if filename == "wordlist.txt":
                    print("Password is a dictionary word and is not secure.")
                    strength = 0
                    print(f"Strength Score: {strength}/5")
                else:
                    print("Password is a common password and is not secure.")
                    strength = 0
                    print(f"Strength Score: {strength}/5")
                found = True
                break

        if found:
            continue

        if len(password) < min_length:  
            strength = 1
            print("Password is too short and is not secure.")
            print(f"Strength Score: {strength}/5")
            continue

        if len(password) > strong_length:
            strength = 5
            print(f"Strength Score: {strength}/5")
            print("Password is long, length trumps complexity this is a good password.")
            continue
        else:
            print("Password length is acceptable, checking complexity...")
            strength = word_complexity(password)
            strength += 1  # Add 1 for length being acceptable

            print(f"Password strength score: {strength}/5")

        if strength == 5:
            print("Password is strong and secure.")
        else:
            print("Password does not meet complexity requirements and is not secure.")
            print("Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")


def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if case_sensitive:
                if line == word:
                    return True
            else:
                if line.lower() == word.lower():
                    return True

    return False


def word_has_character(word, character_list):
    for char in character_list:
        if char in word:
            return True
    return False


def word_complexity(word):
    strength = 0

    if word_has_character(word, LOWER):
        strength += 1
    if word_has_character(word, UPPER):
        strength += 1
    if word_has_character(word, DIGITS):
        strength += 1
    if word_has_character(word, SPECIAL):
        strength += 1

    return strength


def password_strength(password, min_length=10, strong_length=16):
    strength = 0
    if len(password) < min_length:
        strength = 1
    elif len(password) > strong_length:
        strength = 5
    elif word_in_file("wordlist.txt", password) or word_in_file("toppasswords.txt", password):
        strength = 0
    else:
        strength = word_complexity(password)
        strength += 1  # Add 1 for length being acceptable



    return strength


if __name__ == "__main__":
    main()


