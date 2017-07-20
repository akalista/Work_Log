import csv
import re


class CSV:

    def __init__(self):
            self.fieldnames = ['Date of Task', 'Task Name', 'Time Spent', 'Additional Notes']

    def writer(self, date, name, time, notes):
        with open('log.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writerow({'Date of Task': date, 'Task Name': name, 'Time Spent': time, 'Additional Notes': notes})
            csv_file.close()

    #  Appends whole row based on date pattern
    @staticmethod
    def reader(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) in row[0]:
                    output.append(row)
            csv_file.close()
        return output

    #  Appends all dates with no multiples
    @staticmethod
    def date_reader():
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                output.append(row['Date of Task'])
        output = set(output)
        output = list(output)
        csv_file.close()
        return output

    # Appends whole row based on Notes and Name
    @staticmethod
    def reader2(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) in row[1] or str(pattern) in row[3]:
                    output.append(row)
            csv_file.close()
        return output

    # Appends whole row based on REGEX pattern in Notes or Name
    @staticmethod
    def reader3(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if row[0] == "Date of Task" and row[1] == "Task Name" and row[2] ==\
                        "Time Spent" and row[3] == "Additional Notes":
                    pass
                elif re.search(pattern, row[1]) or re.search(pattern, row[3]):
                    output.append(row)
            csv_file.close()
        return output

    #  Appends whole row based on time spent pattern
    @staticmethod
    def reader4(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) == str(row[2]):
                    output.append(row)
            csv_file.close()
        return output

    # Deletes an entry and writes new CSV with remaining entries
    def delete_entry(self, delete_list):
        output = []
        with open('log.csv', newline="") as input_csv:
            reader = csv.DictReader(input_csv, delimiter=',')
            for row in reader:
                if row['Date of Task'] == delete_list[0] and row['Task Name'] == delete_list[1] \
                        and row['Time Spent'] == delete_list[2] and row['Additional Notes'] == delete_list[3]:
                    pass
                else:
                    output.append(row)
            input_csv.close()
        with open("log.csv", "w") as output_csv:
            writer = csv.DictWriter(output_csv, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writeheader()
            for row in output:
                writer.writerow({
                    'Date of Task': row['Date of Task'],
                    'Task Name': row['Task Name'],
                    'Time Spent': row['Time Spent'],
                    'Additional Notes': row['Additional Notes']
                })
            output_csv.close()
