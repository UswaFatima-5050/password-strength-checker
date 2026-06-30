"""
Password Strength Checker
DecodeLabs Industrial Training Kit | Project 1 - Defensive Logic Track

Goal:
    Evaluate whether a given password is WEAK, MEDIUM, or STRONG using
    string handling and conditional logic (no external libraries needed).

Key checks performed:
    1. Length          -> password must be at least 8 characters (anti
                           brute-force baseline from the IPO model slide)
    2. Uppercase letter -> at least one A-Z
    3. Lowercase letter -> at least one a-z
    4. Digit            -> at least one 0-9
    5. Special symbol   -> at least one non-alphanumeric character
    6. Common password  -> rejects well-known leaked/weak passwords
                           (bonus check suggested in the kit's conclusion)

Author: Uswa Fatima
"""

import string
import re

# ---------------------------------------------------------------------------
# Bonus check (mentioned in the kit's Conclusion slide): a small sample of
# extremely common / leaked passwords. In a real product this list would be
# loaded from a much larger "rockyou.txt"-style file.
# ---------------------------------------------------------------------------
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "password1",
    "111111", "123123", "letmein", "iloveyou", "admin", "welcome",
    "monkey", "dragon", "football", "1234567890", "123456789",
}

MIN_LENGTH = 8
SYMBOL_PATTERN = re.compile(r"[^A-Za-z0-9]")  # anything that isn't a letter/digit


def check_length(password: str) -> bool:
    """Return True if password meets the minimum length requirement."""
    return len(password) >= MIN_LENGTH


def has_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def has_symbol(password: str) -> bool:
    return bool(SYMBOL_PATTERN.search(password))


def is_common_password(password: str) -> bool:
    """Bonus: flag passwords found in a common/leaked password list."""
    return password.lower() in COMMON_PASSWORDS


def evaluate_password(password: str) -> dict:
    """
    Run every check against the password and return a results dictionary
    containing each individual check result, a numeric score, and the
    final strength label (Weak / Medium / Strong).
    """
    results = {
        "length_ok": check_length(password),
        "has_upper": has_uppercase(password),
        "has_lower": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_symbol": has_symbol(password),
        "is_common": is_common_password(password),
    }

    # Immediate fail conditions (Zero Point rule from the kit):
    # too short OR found in the common/leaked password list.
    if not results["length_ok"] or results["is_common"]:
        results["score"] = 0
        results["strength"] = "Weak"
        return results

    # Score 1 point for each character-variety category satisfied.
    score = sum([
        results["has_upper"],
        results["has_lower"],
        results["has_digit"],
        results["has_symbol"],
    ])

    # Bonus point for going well beyond the minimum length.
    if len(password) >= 12:
        score += 1

    results["score"] = score

    if score <= 2:
        results["strength"] = "Weak"
    elif score in (3, 4):
        results["strength"] = "Medium"
    else:
        results["strength"] = "Strong"

    return results


def print_report(password: str, results: dict) -> None:
    """Pretty-print the evaluation results to the console."""
    def mark(ok: bool) -> str:
        return "[PASS]" if ok else "[FAIL]"

    print("\n" + "=" * 45)
    print(f" PASSWORD STRENGTH REPORT")
    print("=" * 45)
    print(f" Length (>= {MIN_LENGTH} chars) : {mark(results['length_ok'])}  ({len(password)} chars)")
    print(f" Uppercase letter        : {mark(results['has_upper'])}")
    print(f" Lowercase letter        : {mark(results['has_lower'])}")
    print(f" Number                  : {mark(results['has_digit'])}")
    print(f" Special symbol          : {mark(results['has_symbol'])}")
    print(f" Not a common password   : {mark(not results['is_common'])}")
    print("-" * 45)
    print(f" SCORE      : {results['score']} / 5")
    print(f" STRENGTH   : {results['strength'].upper()}")
    print("=" * 45)


def main():
    print("DecodeLabs - Password Strength Checker")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "exit":
            print("Goodbye!")
            break
        if password == "":
            print("Password cannot be empty. Try again.\n")
            continue

        results = evaluate_password(password)
        print_report(password, results)
        print()


if __name__ == "__main__":
    main()
