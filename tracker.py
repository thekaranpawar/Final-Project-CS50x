import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.csv"
FIELDNAMES = ["date", "type", "amount", "category", "note"]

# Initialization CSV file
if not DATA_FILE.exists():
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()

def add_transaction(t_type, amount, category, note=""):
    """Add a new transaction to data.csv"""
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "type": t_type,
            "amount": amount,
            "category": category,
            "note": note
        })
    print(f"Added {t_type} of {amount} in category '{category}'.")

def list_transactions():
    """List all transactions"""
    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No transactions found.")
        return

    print(f"{'DATE':19} {'TYPE':8} {'AMOUNT':10} {'CATEGORY':15} NOTE")
    print("-" * 70)
    for row in rows:
        print(f"{row['date']:19} {row['type']:8} {row['amount']:10} {row['category']:15} {row['note']}")

def show_summary():
    """Display total income, expenses, and balance"""
    income = 0
    expenses = 0
    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["amount"])
            if row["type"] == "income":
                income += amount
            else:
                expenses += amount

    balance = income - expenses
    print(f"Total Income : {income}")
    print(f"Total Expense: {expenses}")
    print(f"Balance      : {balance}")

def export_data(filename):
    """Export transactions to a specified CSV file"""
    with open(DATA_FILE, "r") as infile, open(filename, "w", newline="") as outfile:
        outfile.write(infile.read())
    print(f"Data exported to {filename}")
