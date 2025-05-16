import time
from cat_variants import commons, rares, mythicals
from tkinter import *
import random
import os
import json

def load_config():
    default_config = {
        "COMMON": 0.7,
        "RARE": 0.2,
        "MYTHICAL": 0.1
    }

    if not os.path.exists("config.json"):
        with open("config.json", "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config

    with open("config.json", "r") as f:
        return json.load(f)


rarity_chances = load_config()

root = Tk()
root.geometry("500x300")
root.configure(bg='#4a4a4a')
root.title("Snowie RNG")

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def home():
    clear()
    welcome_label = Label(root, text="WELCOME", font=("Arial", 30), bg='#424242', fg='white')
    welcome_label.pack()
    root.after(2000, show_home_buttons)

def show_home_buttons():
        spin_btn = Button(root, text='spin', command=spin, bg='#424242', fg='white')
        view_btn = Button(root, text='view inventory',command=view, bg='#424242', fg='white')
        delete_btn = Button(root, text='Delete Snowie', command=delete_snowie_ui, bg='#424242', fg='white')

        spin_btn.pack()
        view_btn.pack()
        delete_btn.pack()


def spin():
     clear()

     result = Label(root, text="", font=("Arial", 18), bg='#424242', fg='white')
     result.pack(pady=20)
     
     def show_kept_message():
         result.config(text=f"You kept a {final_snowie} Snowie.")
         root.after(2000, lambda: [clear(), home()])

     def do_spin(i=0):
        nonlocal final_snowie
        
        if i < 10:
            rarity = random.random()
            if rarity < rarity_chances["COMMON"]:
                snowie = random.choice(commons)
                text = f"Spinning a {snowie} Snowie!"
            elif rarity < rarity_chances["RARE"] + rarity_chances["COMMON"]:
                snowie = random.choice(rares)
                text = f"Spinning a {snowie} Snowie!!"
            else:
                snowie = random.choice(mythicals)
                text = f"Spinning a {snowie} Snowie!!!"


            result.config(text=text)
            final_snowie = snowie
            rarity_result = rarity
            root.after(200, lambda: do_spin(i+1))
        else:
            ask_to_keep(final_snowie)


     def ask_to_keep(snowie):
         keep = Label(root, text="Do you want to keep this Snowie?", font=("Arial", 15), bg='#383838', fg='white')
         keep.pack()
         yes_btn = Button(root, text="yes", command=lambda: keep_snowie(snowie), bg='#383838', fg='white')
         no_btn = Button(root, text="no", command=home, bg='#383838', fg='white')

         yes_btn.pack(pady=5)
         no_btn.pack(pady=5)

     def keep_snowie(snowie):
         with open('inventory.txt', 'a') as file:
             file.write(f"{snowie} Snowie\n")
         result.config(text="Alright...")
         root.after(1000, show_kept_message())

     final_snowie = ""
     do_spin()

def view():
    clear()

    if not os.path.exists("inventory.txt"):
        Label(root, text="You don't have any Snowies yet!", font=("Arial", 16), bg='#4a4a4a', fg='white').pack(pady=10)
        return

    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        Label(root, text="Your inventory is empty!", font=("Arial", 16), bg='#4a4a4a', fg='white').pack(pady=10)
        return

    Label(root, text="Your Snowies", font=("Arial", 24), bg='#4a4a4a', fg='white').pack(pady=10)

    for i, line in enumerate(lines, 1):
        line = line.strip().replace(" Snowie", "")
        if line in commons:
            rarity = "COMMON"
        elif line in rares:
            rarity = "RARE"
        elif line in mythicals:
            rarity = "MYTHICAL"
        else:
            rarity = "UNKNOWN"

        tag = {
            "MYTHICAL": "🔥👑 MYTHICAL 👑🔥",
            "RARE": "😎 RARE 😎",
            "COMMON": "💩 COMMON 💩"
        }.get(rarity, "❓ UNKNOWN ❓")

        text = f"{i}. {line} Snowie ({tag})"
        Label(root, text=text, font=("Arial", 14), bg='#4a4a4a', fg='white').pack(anchor='w', padx=20)

    Button(root, text="Back", command=home, bg='#383838', fg='white').pack(pady=20)

def delete_snowie_ui():
    clear()

    Label(root, text="Delete a Snowie", font=("Arial", 20), bg='#4a4a4a', fg='white').pack(pady=10)

    entry = Entry(root, font=("Arial", 14))
    entry.pack(pady=5)

    feedback = Label(root, text="", font=("Arial", 14), bg='#4a4a4a', fg='white')
    feedback.pack(pady=5)

    def delete():
        name = entry.get().strip().lower()

        if not os.path.exists("inventory.txt"):
            feedback.config(text="No inventory found.")
            return

        with open("inventory.txt", "r") as f:
            lines = f.readlines()

        updated_lines = [line for line in lines if line.strip().split(" ")[0].lower() != name]

        if len(updated_lines) == len(lines):
            feedback.config(text=f"No Snowie named '{name}' found.")
        else:
            with open("inventory.txt", "w") as f:
                f.writelines(updated_lines)
            feedback.config(text=f"Deleted '{name}' Snowie.")
            entry.delete(0, END)

    Button(root, text="Delete", command=delete, bg='#383838', fg='white').pack(pady=5)
    Button(root, text="Back", command=home, bg='#383838', fg='white').pack(pady=5)

home()
root.mainloop()