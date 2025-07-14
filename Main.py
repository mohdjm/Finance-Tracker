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

# Run it
add_expense()