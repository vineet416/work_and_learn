from warrior import WARRIOR
from archer import ARCHER
from wizard import WIZARD


warrior = WARRIOR("Thor", 100, 5, 25)
archer = ARCHER("Legolas", 100, 4, 20)
wizard = WIZARD("Gandalf", 100, 6, 30)


def main():
    print("Game Started! Current Status:")
    while warrior.health > 0 and archer.health > 0 and wizard.health > 0:
        print("\n" + "-" * 50)
        warrior.display_status()
        archer.display_status()
        wizard.display_status()
        print("-" * 50 + "\n")

        print("\n" + "-" * 50)
        print("Choose an action:")
        print("1. Warrior attacks Archer")
        print("2. Archer attacks Wizard")
        print("3. Wizard attacks Warrior")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        print("-" * 50 + "\n")

        if choice == 1:
            print("\n" + "-" * 50)
            warrior.sword_attack(archer)
            print("-" * 50 + "\n")
        elif choice == 2:
            print("\n" + "-" * 50)
            archer.arrow_attack(wizard)
            print("-" * 50 + "\n")
        elif choice == 3:
            print("\n" + "-" * 50)
            wizard.magic_attack(warrior)
            print("-" * 50 + "\n")
        elif choice == 4:
            print("Exiting the game.")
            print("-" * 50 + "\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
