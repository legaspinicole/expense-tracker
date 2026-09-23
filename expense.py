expenses = []


def add_expense(amount, category, description, date):
    expense = {
        "amount": float(amount),
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)

def edit_expense(index, amount, category, description, date):
    if 0 <= index < len(expenses):
        expenses[index] = {
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": date
        }
        return True
    return False

def delete_expense(index):
    if 0 <= index < len(expenses):
         expenses.pop(index)
         return True
    return False


def get_expenses():
    return expenses


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
