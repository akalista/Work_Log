# Import CSV, REGEX, datetime, and Errors class
import csv
import re
import datetime
from Errors import Error


class CSV:
    '''
    CSV class deals with all interactions with the CSV file. Anything that involves
    reading or writing to the file, including editing and deleting entries. Init initializes
    the fieldnames of the CSV file. The rest of the functions read and write from the file
    in different ways depending on what the user needs.
    '''

    # Init initializes the fieldnames to go above entries
    def __init__(self):
            self.fieldnames = ['Date of Task', 'Task Name', 'Time Spent', 'Additional Notes']

    # Writer takes user input and creates a new row or entry
    def writer(self, date, name, time, notes):
        with open('log.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writerow({'Date of Task': date, 'Task Name': name, 'Time Spent': time, 'Additional Notes': notes})
            csv_file.close()

    # Appends whole row based on date pattern
    @staticmethod
    def reader(pattern):
        output = []
        # Opens file to read, looks for user date in row 0, outputs row if match
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) in row[0]:
                    output.append(row)
            csv_file.close()
        return output

    # Appends all dates with no multiples
    @staticmethod
    def date_reader():
        output = []
        # Open file to read, output all 'Date of Tasks'
        with open('log.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                output.append(row['Date of Task'])
        # Take out duplicates, and output list
        output = set(output)
        output = list(output)
        csv_file.close()
        return output

    # Appends whole row based on Notes and Name
    @staticmethod
    def reader2(pattern):
        output = []
        # Open file to read, check if header
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if row[0] == "Date of Task" and row[1] == "Task Name" and row[2] ==\
                        "Time Spent" and row[3] == "Additional Notes":
                    pass
                # If not header output row that matches input
                elif str(pattern) in row[1] or str(pattern) in row[3]:
                    output.append(row)
            csv_file.close()
        return output

    # Appends whole row based on REGEX pattern in Notes or Name
    @staticmethod
    def reader3(pattern):
        output = []
        # Open file to read, check if header
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if row[0] == "Date of Task" and row[1] == "Task Name" and row[2] ==\
                        "Time Spent" and row[3] == "Additional Notes":
                    pass
                # If not header output row that matches input
                elif re.search(pattern, row[1]) or re.search(pattern, row[3]):
                    output.append(row)
            csv_file.close()
        return output

    #  Appends whole row based on time spent pattern
    @staticmethod
    def reader4(pattern):
        output = []
        # Open file to read, output row if input matches
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) == str(row[2]):
                    output.append(row)
            csv_file.close()
        return output

    # Appends whole row based on date range
    @staticmethod
    def reader5(user_date1, user_date2):
        output = []
        # Open file to read, check to see if row is header
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if row[0] != 'Date of Task' and row[1] != 'Task Name' and row[2] != 'Time Spent'\
                        and row[3] != 'Additional Notes':
                    # If row not header and date of entry is between user inputs output row
                    if datetime.datetime.strptime(user_date1, '%m/%d/%y') <= datetime.datetime.strptime(row[0],
                       '%m/%d/%y') <= datetime.datetime.strptime(user_date2, '%m/%d/%y'):
                            output.append(row)
            csv_file.close()
        return output

    # Deletes an entry and writes new CSV with remaining entries
    def delete_entry(self, delete_list):
        output = []
        # Open file
        with open('log.csv', newline="") as input_csv:
            reader = csv.DictReader(input_csv, delimiter=',')
            # If row matches user input don't append, else append whole row
            for row in reader:
                if row['Date of Task'] == delete_list[0] and row['Task Name'] == delete_list[1] \
                        and row['Time Spent'] == delete_list[2] and row['Additional Notes'] == delete_list[3]:
                    pass
                else:
                    output.append(row)
            input_csv.close()
        # Open file to write, write new header
        with open("log.csv", "w") as output_csv:
            writer = csv.DictWriter(output_csv, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writeheader()
            # Write rows in output to new file and close
            for row in output:
                writer.writerow({
                    'Date of Task': row['Date of Task'],
                    'Task Name': row['Task Name'],
                    'Time Spent': row['Time Spent'],
                    'Additional Notes': row['Additional Notes']
                })
            output_csv.close()

    # Edits an entry and writes new CSV with new entry
    def edit_entry(self, edit_list, edit_item):
        error = Error()
        output = []
        # Open file
        with open('log.csv', newline="") as input_csv:
            reader = csv.DictReader(input_csv, delimiter=',')
            for row in reader:
                # If row matches edit list
                if row['Date of Task'] == edit_list[0] and row['Task Name'] == edit_list[1] \
                        and row['Time Spent'] == edit_list[2] and row['Additional Notes'] == edit_list[3]:
                    # Match edit item to different options
                    # Change date
                    if edit_item == 1:
                        new_date = error.time_error()
                        row['Date of Task'] = new_date
                        output.append(row)
                    # Change task name
                    if edit_item == 2:
                        new_task_name = error.empty_task_error()
                        row['Task Name'] = new_task_name
                        output.append(row)
                    # Change time spent
                    if edit_item == 3:
                        new_time = error.time_spent_error()
                        row['Time Spent'] = new_time
                        output.append(row)
                    # Change additional notes
                    if edit_item == 4:
                        new_note = input("What is the new note?\n>>")
                        row['Additional Notes'] = new_note
                        output.append(row)
                # If no match then append original row
                else:
                    output.append(row)
            input_csv.close()
        # Open file to write
        with open("log.csv", "w") as output_csv:
            writer = csv.DictWriter(output_csv, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writeheader()
            # Write output list into new CSV file
            for row in output:
                writer.writerow({
                    'Date of Task': row['Date of Task'],
                    'Task Name': row['Task Name'],
                    'Time Spent': row['Time Spent'],
                    'Additional Notes': row['Additional Notes']
                })
            output_csv.close()
