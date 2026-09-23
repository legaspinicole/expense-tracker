categories = [
    "Food",
    "Transportation",
    "Shopping",
    "Bills"
]


def get_categories():
    return categories


def add_category(category):
    category = category.strip()

    if category and category not in categories:
        categories.append(category)
        return True
    
    return False

def edit_category(index, new_category):
    new_category = new_category.strip()

    if (
        0 <= index < len(categories)
        and new_category
        and new_category not in categories
    ):
        old_category = categories[index]
        categories[index] = new_category

        return old_category, new_category

    return None

def delete_category(index):
    if 0 <= index < len(categories):
        return categories.pop(index)

    return None
