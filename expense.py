from database import expenses_collection


# ============================================================
# ADD EXPENSE
# ============================================================

def add_expense(amount, category, description, date):

    expense = {
        "amount": float(amount),
        "category": category,
        "description": description,
        "date": date
    }

    expenses_collection.insert_one(expense)


# ============================================================
# EDIT EXPENSE
# ============================================================

def edit_expense(index, amount, category, description, date):

    expense_list = list(
        expenses_collection.find().sort("_id", 1)
    )

    if 0 <= index < len(expense_list):

        expense_id = expense_list[index]["_id"]

        expenses_collection.update_one(
            {"_id": expense_id},
            {
                "$set": {
                    "amount": float(amount),
                    "category": category,
                    "description": description,
                    "date": date
                }
            }
        )

        return True

    return False


# ============================================================
# DELETE EXPENSE
# ============================================================

def delete_expense(index):

    expense_list = list(
        expenses_collection.find().sort("_id", 1)
    )

    if 0 <= index < len(expense_list):

        expense_id = expense_list[index]["_id"]

        expenses_collection.delete_one(
            {"_id": expense_id}
        )

        return True

    return False


# ============================================================
# SHOW EXPENSES
# ============================================================

def get_expenses():

    return list(
        expenses_collection.find().sort("_id", 1)
    )


# ============================================================
# CALCULATE TOTAL
# ============================================================

def calculate_total():

    total = 0

    for expense in expenses_collection.find():

        total += expense["amount"]

    return total