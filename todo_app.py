from prettytable import PrettyTable

print("#################TO-DO App###############")
print("\n")
instructions = """                  1:Enter add to add new to-do list.\n 
                  2:Enter del to delete to-do list.\n
                  3:Enter update to update to-do list.\n
                  4:Enter exit to exit from to-do list.\n
                  5:Enter see to check to-do list.\n"""

print(instructions)

to_do_list = []

x = PrettyTable()
x.field_names = ["Items Name"]

def mylist():
    for i in to_do_list:
        x.add_row([i])

    print(x.get_string(title="TO DO LIST"))
    x.clear_rows()

running = True

while running:
    print("\n")
    user_input = input("What do you want to do? \n add \n del \n update \n exit \n see \n").lower()

    if user_input == "add":
        new_todo = input("Enter the task you want to add: ").lower()
        print(f"Your current TO-DO List is {new_todo}")
        to_do_list.append(new_todo)

    elif user_input == "update":
        
            try:
                item_name = input("Please enter the name of the item you want to update: ").lower()
                if item_name in to_do_list:
                    choice = input("Are you sure you want to update: y/n ").lower()
                    if choice == "y":
                        updated_item = input(f"Please enter the name you want to update with {item_name} : " ).lower()
                        index = to_do_list.index(item_name)
                        to_do_list[index] = updated_item
                        print("Your updated to-do list is: ")
                        print("\n")
                        mylist()
                        
                else:
                    print("Item not found")
            except Exception:
                print("Something went wrong")

    elif user_input == "del":
        item_name = input("Please enter the name of the item you want to delete: ").lower()
        if item_name in to_do_list:
            choice = input("Are you sure you want to delete: y/n ").lower()
            if choice == "y":
                to_do_list.remove(item_name)
                print("Your updated to-do list is: ")
                print("\n")
                mylist()
        else:
            print("Item not found")

    elif user_input == "exit":
       choice = input("Are you sure you want to exit? (yes or no): ").lower()
       if choice == "yes":
        print("Thanks! for using TO-DO APP")
        break

        

    elif user_input == "see":
        mylist()

    elif user_input == "":
        print("Please enter something")

    else:
        print("Please insert a valid value")
