def display_menu():
    print("\n" + "="*30)
    print("Shopping List Manager")
    print("="*30)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*30)

def add_item(shopping_list):
    item = input("Enter the item name: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return
    
    item = input("Enter the item name to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"  {index}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("\nGoodbye! Your shopping list has been closed.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()