# Import CSV class and Error class
from CSV import CSV
from Errors import Error


# Class containing all entry functions
class Entry:
    """
    Entry class is used for interaction with an Entry between the work_log and the
    CSV class. Most of the functions in this class simply pass down variables or
    display them in a neater way. Init initializes the CSV and Errors class, and
    the entry class uses user input to create a new entry.
    """

    # Init initializes CSV/Error class to use in other functions
    def __init__(self):
        self.my_csv = CSV()
        self.error = Error()

    # Add an entry to CSV file
    def add(self):
        # Set date, name, time, and notes, check for errors on first 3 (Notes are optional)
        date = self.error.time_error()
        name = self.error.empty_task_error()
        time = self.error.time_spent_error()
        notes = input("Enter any additional notes on the entry (optional)\n>>")
        # Pass down variables to writer in CSV, print confirmation
        self.my_csv.writer(date, name, time, notes)
        input("This entry has been added. Press enter to return to the main menu!")

    # Delete an Entry (pass info)
    def delete(self, to_delete):
        self.my_csv.delete_entry(to_delete)

    # Edit an Entry (pass info)
    def edit(self, list_edit, item_edit):
        self.my_csv.edit_entry(list_edit, item_edit)

    # Search by date Range (pass info)
    def range(self, date1, date2):
        self.my_csv.reader5(date1, date2)

    # Used for appending whole row while looking in entire row
    def list_display(self, look):
        new_list = [x for x in self.my_csv.reader(look)]
        return new_list

    # Used for appending whole row while looking at Task Name and Additional Notes
    def list_display2(self, look):
        new_list = [x for x in self.my_csv.reader2(look)]
        return new_list

    # Used for appending whole row while looking at Task Name and Additional Notes with REGEX
    def list_display3(self, look):
        new_list = [x for x in self.my_csv.reader3(look)]
        return new_list

    # Used for appending whole row while looking at Time Spent
    def list_display4(self, look):
        new_list = [x for x in self.my_csv.reader4(look)]
        return new_list

    # Used to display available dates
    def display_dates(self):
        for x in self.my_csv.date_reader():
            print(x)
