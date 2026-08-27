inventory = {}

def add_item(inventory ,condition="good"):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    condition = input("Enter condition: ")

    inventory[item] = (quantity, condition)
    print("Item Added")

def update_item(inventory):

    item = input("Enter item name: ")

    if item in inventory:
        quantity = int(input("Enter new quantity: "))

        condition = inventory[item][1]
        inventory[item] = (quantity, condition)

        print("Item updated!")

    else:
        print("Item not found!")

def delete_item(inventory):
    item = input("Enter item name: ")
    if item in inventory:
        del inventory[item]
        print("Item deleted!")
    else:
        print("Item not found!")


def search_item(inventory):
    item = input("Enter item name: ")
    if item in inventory:
        print(item , ":" , inventory[item])
    else:
        print("Item not found!")


def print_inventory(inventory):
    print("\nInventory:")
    for item in inventory:
        print(item , ":" , inventory[item])


while True:

    print("\n1. Add Item")
    print("2. Update Quantity")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. Display Inventory")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item(inventory)

    elif choice == "2":
        update_item(inventory)

    elif choice == "3":
        delete_item(inventory)

    elif choice == "4":
        search_item(inventory)

    elif choice == "5":
        print_inventory(inventory)

    elif choice == "6":
        print("Program ended!")
        break

    else:
        print("Invalid choice!")