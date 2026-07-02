import os
from datetime import datetime

JOURNAL_FILE = "journal.txt"


def write_to_journal():
    print("\nEnter your journal entry.")
    print("Type 'exit' on a new line when you are done.\n")

    lines = []

    while True:
        line = input("> ")

        if line.lower() == "exit":
            break

        lines.append(line)

    if not lines:
        print("No entry made.\n")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(JOURNAL_FILE, "a") as f:
        f.write("\n==============================\n")
        f.write(f"Date: {timestamp}\n")
        f.write("==============================\n")

        for line in lines:
            f.write(line + "\n")

        f.write("\n")

    print("Journal entry saved successfully.\n")


def read_journal():
    if not os.path.exists(JOURNAL_FILE):
        print("\nNo journal entries found.\n")
        return

    with open(JOURNAL_FILE, "r") as f:
        content = f.read()

    if content.strip() == "":
        print("\nNo journal entries found.\n")
    else:
        print("\n===== YOUR JOURNAL =====\n")
        print(content)


def main():
    while True:
        print("========== Journal App ==========")
        print("1. Write a Journal Entry")
        print("2. Read Journal Entries")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            write_to_journal()

        elif choice == "2":
            read_journal()

        elif choice == "3":
            print("Thank you for using Journal App. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()