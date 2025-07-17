import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Load existing expenses
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                })
    except FileNotFoundError:
        pass
    return expenses

# Save all expenses to file
def save_expenses(expenses):
    with open(FILENAME, mode="w", newline='') as file:
        fieldnames = ["date", "category", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

# Add a new expense
def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter the category: ").strip()
    amount = float(input("Enter the amount: ").strip())
    new_expense = {"date": date, "category": category, "amount": amount}
    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added and saved.")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
    else:
        print("\n--- Your Expenses ---")
        for exp in expenses:
            print(f"{exp['date']} | {exp['category'].title()} | RM {exp['amount']:.2f}")
        print("----------------------")

# Main loop
def main():
    print("📒 Welcome to Your Finance Tracker (CSV Edition)")
    expenses = load_expenses()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye! Your data is saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
