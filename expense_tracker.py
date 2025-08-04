import json
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.json"

# Load existing expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Transport, Entertainment, etc.): ")
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category.capitalize(),
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View summary
def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense Summary ---")
    total_spending = sum(exp["amount"] for exp in expenses)
    print(f"Total Spending: ₹{total_spending:.2f}")

    # Total by category
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]

    print("\nSpending by Category:")
    for cat, total in category_totals.items():
        print(f"{cat}: ₹{total:.2f}")

    # Spending over time (daily)
    date_totals = {}
    for exp in expenses:
        date_totals[exp["date"]] = date_totals.get(exp["date"], 0) + exp["amount"]

    print("\nSpending by Date:")
    for date, total in date_totals.items():
        print(f"{date}: ₹{total:.2f}")

# Delete an expense (Optional Bonus)
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    print("\n--- Delete Expense ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']}")

    choice = int(input("Enter expense number to delete (0 to cancel): "))
    if 1 <= choice <= len(expenses):
        deleted = expenses.pop(choice - 1)
        save_expenses(expenses)
        print(f"✅ Deleted: {deleted['category']} - ₹{deleted['amount']} on {deleted['date']}")
    else:
        print("Cancelled.")

# Main menu
def main():
    expenses = load_expenses()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
