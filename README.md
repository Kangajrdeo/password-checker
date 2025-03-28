Password Strength Evaluation Tool - User Manual

1. Introduction

The Password Strength Evaluation Tool is designed to help users assess the security of their passwords based on cybersecurity best practices. It identifies weak passwords, evaluates their strength, and checks if they have been compromised in breach databases or wordlists.

2. System Requirements

Operating System: Windows

Python Version: Python 3.10 

Required Libraries: tkinter, re

Additional Files:

rockyou.txt (for dictionary attack simulation)

wordlist.txt (list of commonly used passwords)

3. Installation

Ensure you have Python 3.10+ installed on your system.

Install required dependencies (if needed):

pip install requests

Place the script in the same directory as rockyou.txt and wordlist.txt.

Run the script using:

python test.py

4. Features

4.1 Password Strength Evaluation

Checks if the password meets the NIST SP 800-63B standards:

Minimum 12 characters

Must contain at least 3 of the following:

Uppercase letters (A-Z)

Lowercase letters (a-z)

Numbers (0-9)

Special characters (!@#$%^&* etc.)

Provides feedback on password strength: Weak, Medium, Strong, Critical Risk

4.2 Breach Database & Dictionary Attack Check

Checks if the password appears in a breach database.

Compares against a dictionary of common passwords (rockyou.txt).

5. How to Use

5.1 Graphical User Interface (GUI) Instructions

Launch the program by running test.py.

The GUI window will appear with a text box labeled "Enter your password:".

Type your password and click "Evaluate Password".

A pop-up will display:

Strength rating (Weak/Medium/Strong)

Security feedback

Whether the password was found in breach databases

5.2 Command Line Interface (CLI) Option (If Implemented)

Run the script:

python test.py

Enter your password when prompted.

The tool will evaluate and display:

Strength rating

Security suggestions

Breach check results

6. Troubleshooting

6.1 Common Errors & Solutions

Error Message

Cause

Solution

'utf-8' codec can't decode byte

rockyou.txt contains non-UTF-8 characters

Open rockyou.txt with encoding 'utf-8', errors='ignore'

FileNotFoundError: 'wordlist.txt' not found

Missing wordlist.txt

Ensure the file is in the same directory

ModuleNotFoundError: No module named 'tkinter'

Missing Tkinter library

Install Tkinter (sudo apt install python3-tk for Linux)

7. Security Considerations

Do NOT use real passwords for testing.

Avoid storing sensitive passwords in plain text.

Update the breach database regularly to maintain security.
