import tkinter as tk

# --- Procedural Data Stores ---
categories = ["Category 1", "Category 2", "Category 3", "Category 4"]
category_colors = ["#E5732F", "#5D9CEC", "#505A3E", "#2B62D9"]

transactions = [
    {"name": "Transaction 1", "cat": "Category 1", "date": "09/01/2026", "amount": "- P 180.00"},
    {"name": "Transaction 2", "cat": "Category 2", "date": "09/01/2026", "amount": "- P 180.00"},
    {"name": "Transaction 3", "cat": "Category 3", "date": "09/01/2026", "amount": "- P 180.00"},
]

# --- 1. Root Window Setup ---
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("850x600")
root.configure(bg="#F6F3E6")  # Background matching Figma canvas

# --- 2. Orange Top Header (Logo) ---
header = tk.Frame(root, bg="#E5732F", height=60)
header.pack(fill=tk.X)
header.pack_propagate(False)

logo_text = tk.Label(header, text="(LOGO)", font=("Arial", 20, "bold"), bg="#E5732F", fg="#000000")
logo_text.pack(side=tk.LEFT, padx=20, pady=10)

# --- 3. Main Content Container ---
content = tk.Frame(root, bg="#F6F3E6")
content.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# Left Column (Cards Area)
left_column = tk.Frame(content, bg="#F6F3E6")
left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))

# Right Column (Action Buttons Area)
right_column = tk.Frame(content, bg="#F6F3E6")
right_column.pack(side=tk.RIGHT, fill=tk.Y, anchor="n")

# --- 4. "Total Spent" Card (Top Left) ---
card_total = tk.Frame(left_column, bg="#FFFFFF", padx=15, pady=15)
card_total.pack(fill=tk.X, pady=(0, 15))

label_title = tk.Label(card_total, text="Total spent this month", font=("Arial", 11), fg="#777777", bg="#FFFFFF")
label_title.pack(anchor="w")

label_amount = tk.Label(card_total, text="18, 000", font=("Arial", 30, "bold"), bg="#FFFFFF")
label_amount.pack(anchor="w", pady=(0, 10))

# Category Legend Bar
legend_frame = tk.Frame(card_total, bg="#FFFFFF")
legend_frame.pack(fill=tk.X, pady=(0, 10))

for idx in range(len(categories)):
    box = tk.Label(legend_frame, bg=category_colors[idx], width=2, height=1)
    box.pack(side=tk.LEFT, padx=(0, 4))
    
    lbl = tk.Label(legend_frame, text=categories[idx], font=("Arial", 9), bg="#FFFFFF")
    lbl.pack(side=tk.LEFT, padx=(0, 12))

# Multi-colored Segment Bar (Simulated via placed sub-frames)
bar_container = tk.Frame(card_total, height=12, bg="#E0E0E0")
bar_container.pack(fill=tk.X)

segment_widths = [0.35, 0.25, 0.20, 0.20]  # Width ratios for the bar
current_x = 0.0
for idx in range(len(segment_widths)):
    w = segment_widths[idx]
    seg = tk.Frame(bar_container, bg=category_colors[idx])
    seg.place(relx=current_x, rely=0, relwidth=w, relheight=1.0)
    current_x += w

# --- 5. "Recent Transactions" Card (Bottom Left) ---
card_tx = tk.Frame(left_column, bg="#FFFFFF", padx=15, pady=15)
card_tx.pack(fill=tk.BOTH, expand=True)

label_recent = tk.Label(card_tx, text="Recent transactions", font=("Arial", 11, "bold"), fg="#555555", bg="#FFFFFF")
label_recent.pack(anchor="w", pady=(0, 10))

for item in transactions:
    row = tk.Frame(card_tx, bg="#FFFFFF")
    row.pack(fill=tk.X, pady=6)
    
    # Left Details (Name, Category, Date)
    details = tk.Frame(row, bg="#FFFFFF")
    details.pack(side=tk.LEFT)
    
    t_name = tk.Label(details, text=item["name"], font=("Arial", 10, "bold"), bg="#FFFFFF")
    t_name.pack(anchor="w")
    
    t_sub = tk.Label(details, text=f"{item['cat']}  |{item['date']}", font=("Arial", 8), fg="#777777", bg="#FFFFFF")
    t_sub.pack(anchor="w")
    
    # Right Details (Amount & Edit Icon)
    actions = tk.Frame(row, bg="#FFFFFF")
    actions.pack(side=tk.RIGHT)
    
    t_amt = tk.Label(actions, text=item["amount"], font=("Arial", 10, "bold"), bg="#FFFFFF")
    t_amt.pack(side=tk.LEFT, padx=(0, 6))
    
    t_edit = tk.Button(actions, text="📝", font=("Arial", 8), bd=1, relief=tk.SOLID, bg="#F5F5F5")
    t_edit.pack(side=tk.RIGHT)

# --- 6. Action Buttons (Right Column) ---
btn_add = tk.Button(right_column, text="+ Add expense", font=("Arial", 10, "bold"), bg="#FFFFFF", bd=1, relief=tk.SOLID, padx=15, pady=8)
btn_add.pack(fill=tk.X, pady=(0, 10))

btn_cat = tk.Button(right_column, text="Category", font=("Arial", 10, "bold"), bg="#FFFFFF", bd=1, relief=tk.SOLID, padx=15, pady=8)
btn_cat.pack(fill=tk.X)

# --- 7. Event Loop Execution ---
root.mainloop()
