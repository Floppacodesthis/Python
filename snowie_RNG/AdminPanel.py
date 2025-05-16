import json

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"COMMON": 0.7, "RARE": 0.2, "MYTHICAL": 0.1}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    print("\n✅ Rarity chances updated successfully!\n")

def show_config(config):
    print("\n🎲 Current Rarity Chances:")
    for key, value in config.items():
        print(f" - {key}: {value:.2f}")
    print()

def get_valid_chances():
    while True:
        try:
            common = float(input("Enter COMMON chance (0.0 - 1.0): "))
            rare = float(input("Enter RARE chance (0.0 - 1.0): "))
            mythical = float(input("Enter MYTHICAL chance (0.0 - 1.0): "))

            total = round(common + rare + mythical, 4)
            if total != 1.0:
                print(f"\n⚠️ Total is {total}. It must add up to exactly 1.0. Try again.\n")
                continue

            return {"COMMON": common, "RARE": rare, "MYTHICAL": mythical}

        except ValueError:
            print("❌ Invalid input. Please enter numbers like 0.7, 0.2, etc.\n")

def main():
    print("🔧 Snowie Admin Panel\n" + "-" * 25)
    config = load_config()
    show_config(config)

    choice = input("Do you want to update the chances? (y/n): ").strip().lower()
    if choice == "y":
        new_config = get_valid_chances()
        save_config(new_config)
    else:
        print("No changes made.")

if __name__ == "__main__":
    main()
