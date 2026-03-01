from modules.calculator import Calculator
from modules.notes_manager import NotesManager
from modules.timer import Timer
from modules.file_organizer import FileOrganizer
from modules.backup_manager import BackupManager

import os
import time


def calculator_menu():
    calc = Calculator()

    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", calc.add(a, b))
    elif choice == "2":
        print("Result:", calc.subtract(a, b))
    elif choice == "3":
        print("Result:", calc.multiply(a, b))
    elif choice == "4":
        try:
            print("Result:", calc.divide(a, b))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation.")


def notes_menu():
    notes = NotesManager()

    while True:
        print("\n--- Notes Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            content = input("Enter note: ")
            notes.add_note(content)
            print("Note added successfully!")

        elif choice == "2":
            all_notes = notes.get_all_notes()
            if not all_notes:
                print("No notes available.")
            else:
                for i, note in enumerate(all_notes, 1):
                    print(f"{i}. {note['content']}")

        elif choice == "3":
            content = input("Enter note content to delete: ")
            notes.remove_note(content)
            print("Note deleted (if existed).")

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def timer_menu():
    timer = Timer()

    print("\n--- Timer ---")
    input("Press Enter to start timer...")
    timer.start()
    input("Press Enter to stop timer...")
    elapsed = timer.stop()

    print(f"Time elapsed: {elapsed:.2f} seconds")


def file_organizer_menu():
    organizer = FileOrganizer()

    print("\n--- File Organizer ---")
    print("1. Create File")
    print("2. Delete File")

    choice = input("Enter choice: ")
    filename = input("Enter filename: ")

    if choice == "1":
        content = input("Enter file content: ")
        organizer.create_file(filename, content)
        print("File created successfully!")

    elif choice == "2":
        organizer.delete_file(filename)
        print("File deleted (if existed).")

    else:
        print("Invalid choice.")


def backup_menu():
    manager = BackupManager()

    filename = input("Enter file name to backup: ")

    if os.path.exists(filename):
        manager.backup_file(filename)
        print("Backup created successfully!")
    else:
        print("File does not exist.")


def main():
    while True:
        print("\n===== PERSONAL PRODUCTIVITY SUITE =====")
        print("1. Calculator")
        print("2. Notes Manager")
        print("3. Timer")
        print("4. File Organizer")
        print("5. Backup File")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            calculator_menu()
        elif choice == "2":
            notes_menu()
        elif choice == "3":
            timer_menu()
        elif choice == "4":
            file_organizer_menu()
        elif choice == "5":
            backup_menu()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()