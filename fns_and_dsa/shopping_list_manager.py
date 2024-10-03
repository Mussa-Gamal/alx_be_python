def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input('Enter the item to add: ')
            shopping_list.append(item_name)
            print(f'{item_name} has been added to the Shopping List.')
            pass
        elif choice == '2':
            item_to_remove = input('Enter the item to remove: ')
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f'{item_to_remove} has been removed from the Shopping List.')
            else:
                print(f'{item_to_remove} was not found in the Shopping List.')
            pass
        elif choice == '3':
            # Display the shopping list
            print('')
            print('Your current Shopping List:')
            for index, item in enumerate(shopping_list, start = 1):
                print(f'{index}- {item}')
            print('')
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
