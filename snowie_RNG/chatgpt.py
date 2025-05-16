import time
from cat_variants import commons, rares, mythicals
from tkinter import *
import random

root = Tk()
root.configure(bg='#4a4a4a')
root.geometry("500x400")

# Clear all widgets from the screen
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# Home screen
def home():
    clear()
    welcome_label = Label(root, text="WELCOME", font=("Arial", 30), bg='#4a4a4a', fg='white')
    welcome_label.pack(pady=30)
    root.after(2000, show_home_buttons)

# Show buttons after welcome message
def show_home_buttons():
    spin_btn = Button(root, text='Spin', command=spin, width=20)
    view_btn = Button(root, text='View Inventory', width=20)

    spin_btn.pack(pady=10)
    view_btn.pack(pady=10)

# Spin logic
def spin():
    clear()
    result = Label(root, text="", font=("Arial", 18), bg='#4a4a4a', fg='white')
    result.pack(pady=30)

    keep_label = Label(root, text="", font=("Arial", 15), bg='#4a4a4a', fg='white')
    keep_label.pack()

    def do_spin(i=0):
        nonlocal final_snowie  # We'll assign the final snowie to this
        if i < 10:
            rarity = random.random()
            if rarity < 0.70:
                snowie = random.choice(commons)
                text = f"Spinning a {snowie} Snowie!"
            elif rarity < 0.90:
                snowie = random.choice(rares)
                text = f"Spinning a {snowie} Snowie!!"
            else:
                snowie = random.choice(mythicals)
                text = f"Spinning a {snowie} Snowie!!!"

            result.config(text=text)
            final_snowie = snowie  # Save for use in keep decision
            root.after(200, lambda: do_spin(i + 1))
        else:
            ask_to_keep(final_snowie)

    def ask_to_keep(snowie):
        keep_label.config(text="Do you want to keep this Snowie?")
        yes_btn = Button(root, text="Yes", command=lambda: keep_snowie(snowie), bg="#383838", fg="white")
        no_btn = Button(root, text="No", command=home, bg="#383838", fg="white")

        yes_btn.pack(pady=5)
        no_btn.pack(pady=5)

    def keep_snowie(snowie):
        with open('inventory.txt', 'a') as file:
            file.write(f"{snowie} Snowie\n")
        result.config(text=f"You kept a {snowie} Snowie!")
        root.after(1500, home)

    final_snowie = ""  # placeholder
    do_spin()  # start the spinning process

# Start at home screen
home()
root.mainloop()
