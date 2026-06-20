import os
def view_file():
    try:
        file = open("data.txt", "r")
        content = file.read()
        print("\nFile Content:\n")
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found")
def count_lines():
    try:
        file = open("data.txt", "r")
        lines = file.readlines()
        print("Total Lines:", len(lines))
        file.close()
    except FileNotFoundError:
        print("File not found")
def count_words():
    try:
        file = open("data.txt", "r")
        content = file.read()
        words = content.split()
        print("Total Words:", len(words))
        file.close()
    except FileNotFoundError:
        print("File not found")
def search_word():
    try:
        word = input("Enter word to search: ")
        file = open("data.txt", "r")
        content = file.read()
        if word.lower() in content.lower():
            print("Word Found")
        else:
            print("Word Not Found")
        file.close()
    except FileNotFoundError:
        print("File not found")
def generate_report():
    try:
        file = open("data.txt", "r")
        content = file.read()
        lines = len(content.splitlines())
        words = len(content.split())
        report = open("report.txt", "w")
        report.write("FILE REPORT\n")
        report.write("Total Lines: " + str(lines) + "\n")
        report.write("Total Words: " + str(words) + "\n")
        report.close()
        file.close()
        print("Report Generated Successfully")
    except FileNotFoundError:
        print("File not found")
while True:
    print("\n===== FILE HANDLING SYSTEM =====")
    print("1. View File")
    print("2. Count Lines")
    print("3. Count Words")
    print("4. Search Word")
    print("5. Generate Report")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_file()
    elif choice == "2":
        count_lines()
    elif choice == "3":
        count_words()
    elif choice == "4":
        search_word()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid Choice")