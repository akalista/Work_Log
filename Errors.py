import datetime


class Error:

    def __init__(self):
        pass

    @staticmethod
    def error(x, y):
        while True:
            try:
                user_input = int(input("\n>>"))
                if user_input not in range(x, y):
                    raise ValueError
                break
            except ValueError:
                print("That's an invalid input! Select a number between {} and {}!".format(x, y-1))
        return user_input

    @staticmethod
    def time_error():
        while True:
            try:
                date = input("What was the date of the entry (MM/DD/YY format)?\n>>")
                datetime.datetime.strptime(date, '%m/%d/%y')
                break
            except ValueError:
                print("Incorrect data format!\n")
        return date

    @staticmethod
    def time_spent_error():
        while True:
            try:
                time = int(input("How much time was spent on the task (rounded minutes)?\n>>"))
                break
            except ValueError:
                print("Provide a time rounded in minutes!")
        return time

    @staticmethod
    def empty_task_error():
        while True:
            name = input("What is the entry name?\n>>")
            if not name:
                print("Entry needs a name!\n")
                continue
            else:
                break
        return name

    @staticmethod
    def empty_string_error():
        while True:
            string = input("What is the string to search by?\n>>")
            if not string:
                print("Please enter a string to search by!\n")
                continue
            else:
                break
        return string


