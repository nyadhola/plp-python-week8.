
# Personal Mini-Toolkit
# This program provides three useful tools through a menu.

def calculator():
    """Calculate the result of two numbers."""
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"The answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


def todo_list():
    """Allow the user to add, view, and remove tasks."""
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully.")
                    else:
                        print("That task number is not on the list.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


def number_checker():
    """Check whether a number is even or odd and its sign."""
    print("\n--- Number Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print("The number is zero.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: repeat until the user chooses to quit.
def main():
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n===== PERSONAL MINI-TOOLKIT =====")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            number_checker()
        elif choice == "4":
            print("Thank you for using the toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Start the program.
if __name__ == "__main__":
    main()