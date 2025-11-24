def display_menu():
    print("\n" + "="*40)
    print("Shopping List Manager")
    print("="*40)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*40)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item name to add: ").strip()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"✓ '{item}' has been added to the list.")
            else:
                print("✗ Item name cannot be empty. Please try again.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("✗ Your shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item name to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"✓ '{item}' has been removed from the list.")
                else:
                    print(f"✗ '{item}' not found in the shopping list.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("\n📋 Your shopping list is empty.")
            else:
                print("\n📋 Current Shopping List:")
                print("-" * 40)
                for i, item in enumerate(shopping_list, 1):
                    print(f"   {i}. {item}")
                print("-" * 40)
                print(f"Total items: {len(shopping_list)}")
                
        elif choice == '4':
            print("\nGoodbye!")
            break
            
        else:
            print("✗ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()