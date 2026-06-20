Password Generator & Strength Checker

Project Overview

Password Generator & Strength Checker is a Python-based console application developed as part of the CodeVedX Python Programming Internship.

This project helps users generate secure passwords and evaluate password strength based on password length and character complexity.

Features

- Generate random passwords
- User-defined password length
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special characters
- Password strength evaluation
- Menu-driven console application
- Input validation using exception handling

Technologies Used

- Python 3
- random module
- string module

How the System Works

Password Generation

The user enters:

- Password length
- Whether to include uppercase letters
- Whether to include lowercase letters
- Whether to include numbers
- Whether to include special characters

The system generates a random password based on the selected options.

Password Strength Checking

The generated or entered password is analyzed using the following criteria:

1. Password length
2. Uppercase letters
3. Lowercase letters
4. Numbers
5. Special characters

Based on the score, the password is classified as:

- Weak
- Medium
- Strong

Strength Evaluation Logic

Score| Strength
0 – 2| Weak
3 – 4| Medium
5| Strong

Error Handling

The application includes:

- Input validation
- Invalid menu choice handling
- Invalid password length handling
- Character type selection validation

Project Structure

Password_Generator/

├── password_generator.py

└── README.md

How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the command:

python password_generator.py

4. Select an option from the menu.
5. Generate a password or check password strength.

Sample Output

===== PASSWORD GENERATOR & STRENGTH CHECKER =====

1. Generate Password
2. Check Password Strength
3. Exit

Enter your choice: 1

Enter password length: 12

Include Uppercase Letters? (y/n): y

Include Lowercase Letters? (y/n): y

Include Numbers? (y/n): y

Include Special Characters? (y/n): y

Generated Password: A@7kLm#9Pq2!

Password Strength: Strong

Learning Outcomes

Through this project, the following concepts were practiced:

- Functions
- Loops
- Conditional Statements
- String Handling
- Random Password Generation
- Input Validation
- Exception Handling
- Modular Programming

Author

Swetha R

CodeVedX Python Programming Internship