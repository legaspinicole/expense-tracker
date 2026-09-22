```python
import tkinter as tk


# ============================================================
# PROCEDURAL DATA STORES
# ============================================================

categories = [
    "Category 1",
    "Category 2",
    "Category 3",
    "Category 4"
]

category_colors = [
    "#E5732F",
    "#5D9CEC",
    "#505A3E",
    "#2B62D9"
]

transactions = [
    {
        "name": "Transaction 1",
        "cat": "Category 1",
        "date": "09/01/2026",
        "amount": "- P 180.00"
    },
    {
        "name": "Transaction 2",
        "cat": "Category 2",
        "date": "09/01/2026",
        "amount": "- P 180.00"
    },
    {
        "name": "Transaction 3",
        "cat": "Category 3",
        "date": "09/01/2026",
        "amount": "- P 180.00"
    }
]


# ============================================================
# PROCEDURAL ACTION FUNCTIONS
# ============================================================

def add_expense():
    """Temporary function for the Add Expense button."""
    print("Add Expense selected")


def open_categories():
    """Temporary function for the Category button."""
    print("Category selected")


def edit_transaction(transaction):
    """Temporary function for editing a transaction."""
    print("Edit selected:", transaction["name"])


# ============================================================
# HEADER
# ============================================================

def create_header(parent):
    """Creates the orange header and logo."""

    header = tk.Frame(
        parent,
        bg="#E5732F",
        height=60
    )

    header.pack(
        fill=tk.X
    )

    header.pack_propagate(False)

    logo_text = tk.Label(
        header,
        text="(LOGO)",
        font=("Arial", 20, "bold"),
        bg="#E5732F",
        fg="#000000"
    )

    logo_text.pack(
        side=tk.LEFT,
        padx=20,
        pady=10
    )


# ============================================================
# TOTAL SPENDING CARD
# ============================================================

def create_total_card(parent):
    """Creates the total spending card."""

    card_total = tk.Frame(
        parent,
        bg="#FFFFFF",
        padx=15,
        pady=15
    )

    card_total.pack(
        fill=tk.X,
        pady=(0, 15)
    )

    label_title = tk.Label(
        card_total,
        text="Total spent this month",
        font=("Arial", 11),
        fg="#777777",
        bg="#FFFFFF"
    )

    label_title.pack(
        anchor="w"
    )

    label_amount = tk.Label(
        card_total,
        text="18,000",
        font=("Arial", 30, "bold"),
        bg="#FFFFFF"
    )

    label_amount.pack(
        anchor="w",
        pady=(0, 10)
    )

    create_category_legend(card_total)

    create_category_bar(card_total)


# ============================================================
# CATEGORY LEGEND
# ============================================================

def create_category_legend(parent):
    """Creates the category color legend."""

    legend_frame = tk.Frame(
        parent,
        bg="#FFFFFF"
    )

    legend_frame.pack(
        fill=tk.X,
        pady=(0, 10)
    )

    for index in range(len(categories)):

        color_box = tk.Label(
            legend_frame,
            bg=category_colors[index],
            width=2,
            height=1
        )

        color_box.pack(
            side=tk.LEFT,
            padx=(0, 4)
        )

        category_label = tk.Label(
            legend_frame,
            text=categories[index],
            font=("Arial", 9),
            bg="#FFFFFF"
        )

        category_label.pack(
            side=tk.LEFT,
            padx=(0, 12)
        )


# ============================================================
# CATEGORY SPENDING BAR
# ============================================================

def create_category_bar(parent):
    """Creates the multi-colored category spending bar."""

    bar_container = tk.Frame(
        parent,
        height=12,
        bg="#E0E0E0"
    )

    bar_container.pack(
        fill=tk.X
    )

    bar_container.pack_propagate(False)

    segment_widths = [
        0.35,
        0.25,
        0.20,
        0.20
    ]

    current_x = 0.0

    for index in range(len(segment_widths)):

        segment = tk.Frame(
            bar_container,
            bg=category_colors[index]
        )

        segment.place(
            relx=current_x,
            rely=0,
            relwidth=segment_widths[index],
            relheight=1.0
        )

        current_x += segment_widths[index]


# ============================================================
# TRANSACTION ROW
# ============================================================

def create_transaction(parent, transaction):
    """Creates one transaction row."""

    row = tk.Frame(
        parent,
        bg="#FFFFFF"
    )

    row.pack(
        fill=tk.X,
        pady=6
    )

    # Transaction details

    details = tk.Frame(
        row,
        bg="#FFFFFF"
    )

    details.pack(
        side=tk.LEFT
    )

    transaction_name = tk.Label(
        details,
        text=transaction["name"],
        font=("Arial", 10, "bold"),
        bg="#FFFFFF"
    )

    transaction_name.pack(
        anchor="w"
    )

    transaction_sub = tk.Label(
        details,
        text=f"{transaction['cat']}  |  {transaction['date']}",
        font=("Arial", 8),
        fg="#777777",
        bg="#FFFFFF"
    )

    transaction_sub.pack(
        anchor="w"
    )

    # Transaction amount and edit button

    actions = tk.Frame(
        row,
        bg="#FFFFFF"
    )

    actions.pack(
        side=tk.RIGHT
    )

    amount = tk.Label(
        actions,
        text=transaction["amount"],
        font=("Arial", 10, "bold"),
        bg="#FFFFFF"
    )

    amount.pack(
        side=tk.LEFT,
        padx=(0, 6)
    )

    edit_button = tk.Button(
        actions,
        text="Edit",
        font=("Arial", 8),
        bd=1,
        relief=tk.SOLID,
        bg="#F5F5F5",
        command=lambda t=transaction: edit_transaction(t)
    )

    edit_button.pack(
        side=tk.RIGHT
    )


# ============================================================
# RECENT TRANSACTIONS CARD
# ============================================================

def create_transactions_card(parent):
    """Creates the Recent Transactions section."""

    card_transactions = tk.Frame(
        parent,
        bg="#FFFFFF",
        padx=15,
        pady=15
    )

    card_transactions.pack(
        fill=tk.BOTH,
        expand=True
    )

    recent_label = tk.Label(
        card_transactions,
        text="Recent transactions",
        font=("Arial", 11, "bold"),
        fg="#555555",
        bg="#FFFFFF"
    )

    recent_label.pack(
        anchor="w",
        pady=(0, 10)
    )

    for transaction in transactions:

        create_transaction(
            card_transactions,
            transaction
        )


# ============================================================
# ACTION BUTTONS
# ============================================================

def create_action_buttons(parent):
    """Creates the action buttons on the right side."""

    add_button = tk.Button(
        parent,
        text="+ Add expense",
        font=("Arial", 10, "bold"),
        bg="#FFFFFF",
        bd=1,
        relief=tk.SOLID,
        padx=15,
        pady=8,
        command=add_expense
    )

    add_button.pack(
        fill=tk.X,
        pady=(0, 10)
    )

    category_button = tk.Button(
        parent,
        text="Category",
        font=("Arial", 10, "bold"),
        bg="#FFFFFF",
        bd=1,
        relief=tk.SOLID,
        padx=15,
        pady=8,
        command=open_categories
    )

    category_button.pack(
        fill=tk.X
    )


# ============================================================
# MAIN CONTENT
# ============================================================

def create_main_content(parent):
    """Creates the main content area."""

    content = tk.Frame(
        parent,
        bg="#F6F3E6"
    )

    content.pack(
        fill=tk.BOTH,
        expand=True,
        padx=30,
        pady=20
    )

    # Left column

    left_column = tk.Frame(
        content,
        bg="#F6F3E6"
    )

    left_column.pack(
        side=tk.LEFT,
        fill=tk.BOTH,
        expand=True,
        padx=(0, 20)
    )

    # Right column

    right_column = tk.Frame(
        content,
        bg="#F6F3E6"
    )

    right_column.pack(
        side=tk.RIGHT,
        fill=tk.Y,
        anchor="n"
    )

    # Create sections

    create_total_card(left_column)

    create_transactions_card(left_column)

    create_action_buttons(right_column)


# ============================================================
# MAIN GUI FUNCTION
# ============================================================

def create_gui():
    """Creates and starts the Expense Tracker GUI."""

    root = tk.Tk()

    root.title("Expense Tracker")

    root.geometry("850x600")

    root.configure(
        bg="#F6F3E6"
    )

    create_header(root)

    create_main_content(root)

    root.mainloop()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    create_gui()
```
