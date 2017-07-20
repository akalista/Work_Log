import os
import re
from Errors import Error
from Entry import Entry


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    input("Press enter to return to the main menu!")


def display(list_of_lists, header_list):
    for entries in list_of_lists:
        count = 0
        for variables in entries:
            variables1 = header_list[count] + variables
            entries[count] = variables1
            count += 1
    return list_of_lists


def strip(delete_list):
    string0, string1, string2, string3 = delete_list[0], delete_list[1], delete_list[2], delete_list[3]
    string0, string1, string2, string3 = string0[14:], string1[11:], string2[12:], string3[18:]
    delete_list2 = [string0, string1, string2, string3]
    return delete_list2


def iteration_menu(list_object):
    list_length, running = len(list_object), True
    headers = ['Date of Task: ', 'Task Name: ', 'Time Spent: ', 'Additional Notes: ']
    display(list_object, headers)
    while running:
        if list_length == 0:
            break
        run1, index, back_index = True, 1, -1
        print(re.sub("(.{60})", "\\1\n", ('\n'.join(list_object[0])), 0))
        while run1:
            user_in = input("\nWould you like to see the [N]ext object, [P]revious object, go [B]ack,\n"
                            "[E]dit the entry, or [D]elete the entry?\n>>")
            clear_screen()
            if user_in.upper() == "N":
                if 0 <= index < list_length:
                    print(re.sub("(.{60})", "\\1\n", '\n'.join(list_object[index]), 0))
                    index += 1
                    back_index += 1
                else:
                    print("There are no more entries, look at a previous entry or go back to the main menu.\n")
                    continue
            elif user_in.upper() == "P":
                if back_index >= 0:
                    print(re.sub("(.{60})", "\\1\n", '\n'.join(list_object[back_index]), 0))
                    index -= 1
                    back_index -= 1
                else:
                    print("There are no more entries, look at the next entry or go back to the main menu.\n")
                    continue
            elif user_in.upper() == "B":
                run1 = False
                running = False
                main_menu()
            elif user_in.upper() == "D":
                delete_item = strip(list_object[index - 1])
                entry.delete(delete_item)
                print("Item has been deleted!")
                main_menu()
                running = False
                break
            # NEED WORK HERE
            elif user_in.upper() == "E":
                pass


if __name__ == '__main__':

    run = True
    error = Error()
    entry = Entry()
    while run:
        print("Welcome to the work log! Options are listed below!")
        print("1: Add new entry\n2: Lookup previous entry\n3: Exit the program")
        main_choice = error.error(1, 4)
        clear_screen()
        # Choice is to add Entry
        if main_choice == 1:
            entry.add()
            clear_screen()
        # Choice is to look up Entry
        elif main_choice == 2:
            print("Would you like to look up pattern by:\n1: Date\n2: Time Spent\n"
                  "3: Exact Search\n4: Regex Pattern\n>>")
            user_input1 = error.error(1, 5)
            #  By Date
            if user_input1 == 1:
                clear_screen()
                print("Available dates are:\n")
                # Display available dates, check date for errors and get date
                entry.display_dates()
                print("\n")
                user_date = error.time_error()
                # Create list from entry display, clear screen, start iteration menu
                mah_list = entry.list_display(user_date)
                clear_screen()
                iteration_menu(mah_list)
                clear_screen()
            # By Time Spent
            elif user_input1 == 2:
                clear_screen()
                user_input2 = error.time_spent_error()
                mah_list2 = entry.list_display4(user_input2)
                print("The tasks that match that time length are below:\n")
                iteration_menu(mah_list2)
                clear_screen()
            # By Entered String
            elif user_input1 == 3:
                clear_screen()
                user_input3 = error.empty_string_error()
                mah_list3 = entry.list_display2(user_input3)
                iteration_menu(mah_list3)
                clear_screen()
            # Search by REGEX pattern
            elif user_input1 == 4:
                clear_screen()
                user_input4 = error.empty_string_error()
                mah_list4 = entry.list_display3(user_input4)
                iteration_menu(mah_list4)
                clear_screen()
        elif main_choice == 3:
            print("Goodbye!")
            run = False

