from cat_variants import commons, rares, mythicals
import os
import time
import random

def get_rarity(name):
    if name in mythicals:
        return "MYTHICAL"
    elif name in rares:
        return "RARE"
    else:
        return "COMMON"

def home():
    while True:
        print("\nWould you like to spin or view your Snowies?")
        operation = input("(spin/view/quit): ").strip().lower()

        if operation == 'spin':
            spin()
        elif operation == 'view':
            view()
        elif operation == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def spin():
    rarity_chance = random.random()

    if rarity_chance < 0.75:
        snowie = random.choice(commons)
    elif rarity_chance < 0.95:
        snowie = random.choice(rares)
    else:
        snowie = random.choice(mythicals)

    rarity = get_rarity(snowie)

    print("\nRolling", end='')
    for _ in range(3):
        time.sleep(0.4)
        print(".", end='', flush=True)

    print(f"\nYou rolled a {snowie} Snowie! ({rarity})")

    while True:
        decision = input("Do you want to keep it? (yes/no): ").strip().lower()
        if decision == 'yes':
            with open("inventory.txt", "a") as file:
                file.write(f"{snowie} | {rarity}\n")
            print("Snowie saved to your inventory!")
            break
        elif decision == 'no':
            print("Snowie discarded.")
            break
        else:
            print("Please type 'yes' or 'no'.")

def view():
    if not os.path.exists("inventory.txt"):
        print("You don't have any Snowies yet!")
        return

    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("Your inventory is empty!")
        return

    print("\nYour Snowies:")
    print("-" * 30)
    for i, line in enumerate(lines, 1):
        if "|" in line:
            name, rarity = line.strip().split(" | ")
            tag = {
                "MYTHICAL": "🔥👑 MYTHICAL 👑🔥",
                "RARE": "😎 RARE 😎",
                "COMMON": "💩 COMMON 💩"
            }.get(rarity.upper(), "UNKNOWN")
            print(f"{i}. {name} Snowie ({tag})")
        else:
            print(f"{i}. {line.strip()} (INVALID FORMAT)")
    print("-" * 30)

if __name__ == "__main__":
    home()
