# Import OS, REGEX, and other classes
import os
import re
from Errors import Error
from Entry import Entry
from CSV import CSV


# Clear Screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Menu function
def main_menu():
    input("Press enter to return to the main menu!")


# Creates a more pleasant display for the iteration menu
def display(list_of_lists, header_list):
    # For loops combine list_of_lists and header_list into a readable list to display
    for entries in list_of_lists:
        count = 0
        for variables in entries:
            variables1 = header_list[count] + variables
            entries[count] = variables1
            count += 1
    return list_of_lists


# Strips the headers off the delete_list
def strip(delete_list):
    # Slice indexes are specific to headers
    string0, string1, string2, string3 = delete_list[0], delete_list[1], delete_list[2], delete_list[3]
    string0, string1, string2, string3 = string0[14:], string1[11:], string2[12:], string3[18:]
    delete_list2 = [string0, string1, string2, string3]
    return delete_list2


# Iteration menu for browsing entries
def iteration_menu(list_object):
    '''
    The iteration menu function provides a way for the user of the program to
    scroll through the options they are given in a more pleasant visual way. Each
    Entry that the user scrolls through will be able to be deleted and edited. The
    menu runs off several while loops and a couple of indexes that keep track of
    the users place in the incoming lists.
    '''

    # Set incoming list length, loop to True, headers list, and create the display for the menu
    list_length, running = len(list_object), True
    headers = ['Date of Task: ', 'Task Name: ', 'Time Spent: ', 'Additional Notes: ']
    display(list_object, headers)
    # First running loop
    while running:
        # If there are no matches break loop and go to main menu
        if list_length == 0:
            print("Looks like your search found no matches, sorry!\n")
            main_menu()
            break
        # Set indexes, second while loop to True, and print the first item in the list
        # REGEX if list chars run over 60, newline starts
        run1, index, back_index = True, 1, -1
        print(re.sub("(.{60})", "\\1\n", ('\n'.join(list_object[0])), 0))
        while run1:
            # If list length is 1, special menu presented with no options to scroll, if to correct for mistakes
            if list_length == 1:
                user_in = input("\nWould you like to go [B]ack, [E]dit the entry, or [D]elete the entry?\n>>")
                if user_in.upper() not in ['B', 'E', 'D']:
                    print("Only one entry available, choose from the given options!")
                    continue
            # If list length is greater than 1, other menu appears, all options preset
            else:
                user_in = input("\nWould you like to see the [N]ext object, [P]revious object, go [B]ack,\n"
                                "[E]dit the entry, or [D]elete the entry?\n>>")
            clear_screen()

            # If user selects 'N", and proper conditions met, the entry at 'index' is shown
            if user_in.upper() == "N":
                if 0 <= index < list_length:
                    print(re.sub("(.{60})", "\\1\n", '\n'.join(list_object[index]), 0))
                    # Index and back_index += 1 after print
                    index += 1
                    back_index += 1
                # Message shown if no more entries
                else:
                    print("There are no more entries to browse through!\n")
                    continue

            # If user selects 'P' and proper conditions met, entry at 'back_index' is shown
            elif user_in.upper() == "P":
                if back_index >= 0:
                    print(re.sub("(.{60})", "\\1\n", '\n'.join(list_object[back_index]), 0))
                    # Index and back_index +=1 after print
                    index -= 1
                    back_index -= 1
                # Message shown if no more entries
                else:
                    print("There are no more entries, look at the next entry or go back to the main menu.\n")
                    continue

            # If user selects 'B' both loops set to false and main menu presented
            elif user_in.upper() == "B":
                run1 = False
                running = False
                main_menu()

            # If user selects 'D' the list at index - 1 is stripped of the header
            elif user_in.upper() == "D":
                delete_item = strip(list_object[index - 1])
                # Delete entry is passed down via Entry()
                entry.delete(delete_item)
                # Print Delete confirmation and go back to main menu
                print("Item has been deleted!")
                main_menu()
                running = False
                break

            # If user selects 'E', the list at index - 1 is stripped of the header
            elif user_in.upper() == "E":
                edit_list = strip(list_object[index - 1])
                # Options appear for the list edit, verify list option with error check
                print("What would you like to edit:\n1: Date of Task\n2: Task Name"
                      "\n3: Time Spent\n4: Additional Notes")
                edit_item = error.error(1, 5)
                # Edit is passed down via Entry() with the edit list and item
                entry.edit(edit_list, edit_item)
                # Edit confirmation and go back to main menu
                print("Item has been edited!")
                main_menu()
                running = False
                break

# Main()
if __name__ == '__main__':
    '''
    Main iteration menu is given to the users the the options to add an entry,
    look up and old entry, or exit the program. Looking up an old entry yields even
    more options on how to look up the entry.
    '''
    # Run set to True, create other class instances
    run = True
    error = Error()
    entry = Entry()
    csv = CSV()
    # While to correct for mistakes
    while run:
        # Print work log menu with options, check for errors and clear screen
        print("Welcome to the work log! Options are listed below!")
        print("1: Add new entry\n2: Lookup previous entry\n3: Exit the program")
        main_choice = error.error(1, 4)
        clear_screen()
        # Choice is to add Entry, use entry.add() to add
        if main_choice == 1:
            entry.add()
            clear_screen()
        # Choice is to look up Entry
        elif main_choice == 2:
            # Print menu of choices to look up by, check for errors
            print("Would you like to look up pattern by:\n1: Date\n2: Time Spent\n"
                  "3: Exact Search\n4: Regex Pattern\n5: Date Range\n>>")
            user_input1 = error.error(1, 6)
            # Look up by date
            if user_input1 == 1:
                clear_screen()
                # Display available dates, check date for errors and get date
                print("Available dates are:\n")
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
                # Get time spent user input, check for errors, create list of entries that match minutes
                user_input2 = error.time_spent_error()
                mah_list2 = entry.list_display4(user_input2)
                # Print available tasks that match minutes and start iteration menu
                print("The tasks that match that time length are below:\n")
                iteration_menu(mah_list2)
                clear_screen()
            # By Entered String
            elif user_input1 == 3:
                clear_screen()
                # Get string user input, check for errors, create list of entries that match string
                user_input3 = error.empty_string_error()
                mah_list3 = entry.list_display2(user_input3)
                # Start iteration menu
                iteration_menu(mah_list3)
                clear_screen()
            # Search by REGEX pattern
            elif user_input1 == 4:
                clear_screen()
                # Get REGEX user input, create list of entries that match REGEX patters
                user_input4 = error.empty_string_error()
                mah_list4 = entry.list_display3(user_input4)
                # Start iteration menu
                iteration_menu(mah_list4)
                clear_screen()
            # Search by date range
            elif user_input1 == 5:
                clear_screen()
                # Get date1 and 2 inputs, check for errors, and create list of entries
                date1 = error.time_error2('start')
                date2 = error.time_error2('end')
                mah_list5 = csv.reader5(date1, date2)
                # Start iteration menu
                iteration_menu(mah_list5)
                clear_screen()
        # Choice is to exit program
        elif main_choice == 3:
            # Exit program by setting loop to False
            print("Goodbye!")
            run = False

