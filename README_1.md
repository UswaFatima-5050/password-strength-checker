# 🔐 Password Strength Checker

**DecodeLabs Industrial Training Kit — Project 1 (Defensive Logic Track)**
Batch 2026 | Cyber Security

## 📌 Overview

A Python command-line tool that evaluates whether a password is **Weak**,
**Medium**, or **Strong** based on length and character-variety rules. This
project focuses on core security logic — string handling, conditional
checks, and basic entropy concepts — before moving on to hashing and
encryption (Project 2).

## ✅ Features

- Checks password **length** (minimum 8 characters)
- Checks for **uppercase**, **lowercase**, **digits**, and **special symbols**
- Flags passwords found in a **common/leaked password list** (bonus check)
- Awards a bonus point for passwords **12+ characters** long
- Prints a clean pass/fail **report** with a final strength score and label
- Simple interactive loop — keep checking passwords until you type `exit`

## 🧠 How Strength Is Scored

| Check | Points |
|---|---|
| Uppercase letter present | +1 |
| Lowercase letter present | +1 |
| Digit present | +1 |
| Special symbol present | +1 |
| Length ≥ 12 characters | +1 (bonus) |

**Immediate fail (Weak):** password is under 8 characters, **or** it matches
a known common/leaked password.

| Score | Strength |
|---|---|
| 0 – 2 | Weak |
| 3 – 4 | Medium |
| 5 | Strong |

## 🚀 How to Run

Requires Python 3.6+. No external libraries needed.

```bash
python3 password_checker.py
```

Example session:

```
DecodeLabs - Password Strength Checker
Type 'exit' to quit.

Enter a password to check: P@ssword123!Strong

=============================================
 PASSWORD STRENGTH REPORT
=============================================
 Length (>= 8 chars) : [PASS]  (18 chars)
 Uppercase letter        : [PASS]
 Lowercase letter        : [PASS]
 Number                  : [PASS]
 Special symbol          : [PASS]
 Not a common password   : [PASS]
---------------------------------------------
 SCORE      : 5 / 5
 STRENGTH   : STRONG
=============================================
```

## 📂 Project Structure

```
password-strength-checker/
├── password_checker.py   # main program
└── README.md             # this file
```

## 🛠 Key Skills Demonstrated

- String handling & iteration
- Conditional / boolean logic
- Regular expressions (for symbol detection)
- Basic security awareness: entropy, common-password blacklisting, and
  brute-force risk from short passwords

## 🔮 Possible Future Improvements

- Load a much larger leaked-password list (e.g. `rockyou.txt`)
- Calculate true entropy in bits using the character pool size
- Add a GUI (Tkinter) front end
- Move on to **Project 2: Hashing & Encryption** (Argon2id) per the
  DecodeLabs roadmap

---

*Built as part of the DecodeLabs Cyber Security Industrial Training Kit
(Batch 2026).*
