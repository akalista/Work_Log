from CSV import CSV
from Errors import Error


class Entry:

    def __init__(self):
        self.my_csv = CSV()

    def add(self):
        error = Error()

        date = error.time_error()
        name = error.empty_task_error()
        time = error.time_spent_error()
        notes = input("Enter any additional notes on the entry (optional)\n>>")

        self.my_csv.writer(date, name, time, notes)
        input("This entry has been added. Press enter to return to the main menu!")

    def delete(self):
        pass

    # Used for appending whole row while looking in entire row
    def list_display(self, look):
        new_list = [x for x in self.my_csv.reader(look)]
        return new_list

    # Used for appending whole row while looking at Task Name and Additional Notes
    def list_display2(self, look):
        new_list = [x for x in self.my_csv.reader2(look)]
        return new_list

    def list_display3(self, look):
        new_list = [x for x in self.my_csv.reader3(look)]
        return new_list

    # Used to display available dates
    def display_dates(self):
        for x in self.my_csv.date_reader():
            print(x)


