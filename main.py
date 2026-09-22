from expense import add_expense, get_expenses, calculate_total
from category import get_categories


def main():
    print("Expense Tracker")
    print("----------------")

    add_expense(
        180,
        "Food",
        "Lunch",
        "09/23/2026"
    )

    print("\nRecent Transactions:")

    for expense in get_expenses():
        print(
            expense["description"],
            "- ₱",
            expense["amount"]
        )

    print("\nTotal spent: ₱", calculate_total())

    print("\nCategories:")
    print(get_categories())


if __name__ == "__main__":
    main()
