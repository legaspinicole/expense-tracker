expenses = []


def add_expense(amount, category, description, date):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)


def get_expenses():
    return expenses


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
