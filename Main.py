import csv
from datetime import datetime

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount (RM): "))
    category = input("Category (e.g. Therapy, Debt, Food): ")
    date = input("Date (YYYY-MM-DD, leave blank for today): ")

    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category, date])

    print("✅ Expense added!")

def view_summary():
    total = 0
    category_totals = {}

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    name, amount, category, date = row
                    amount = float(amount)
                    total += amount
                    category_totals[category] = category_totals.get(category, 0) + amount
                except ValueError:
                    continue  # skip bad lines

        print("\n💸 Total Expenses: RM{:.2f}".format(total))
        print("📊 Breakdown by Category:")
        for category, amt in category_totals.items():
            print(f"- {category}: RM{amt:.2f}")
        print()

    except FileNotFoundError:
        print("⚠️ No expense data found.\n")

def show_menu():
    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")
# Run the menu
show_menu()
