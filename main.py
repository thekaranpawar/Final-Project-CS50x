import argparse
from tracker import add_transaction, list_transactions, show_summary, export_data

# Command-line argument parsing
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # command
    add_parser = subparsers.add_parser("add", help="Add a new transaction")
    add_parser.add_argument("--type", required=True, choices=["income", "expense"], help="Transaction type")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the transaction")
    add_parser.add_argument("--category", required=True, help="Category, e.g., food, rent")
    add_parser.add_argument("--note", default="", help="Optional note about this transaction")

    # list command
    subparsers.add_parser("list", help="List all transactions")

    # summary command
    subparsers.add_parser("summary", help="Show summary of income, expenses, and balance")

    # export command
    export_parser = subparsers.add_parser("export", help="Export all data to a CSV file")
    export_parser.add_argument("--filename", required=True, help="Output filename for exported data")

    args = parser.parse_args()

    if args.command == "add":
        add_transaction(args.type, args.amount, args.category, args.note)
    elif args.command == "list":
        list_transactions()
    elif args.command == "summary":
        show_summary()
    elif args.command == "export":
        export_data(args.filename)

if __name__ == "__main__":
    main()

