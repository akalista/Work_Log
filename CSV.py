import csv
import re


class CSV:

    def __init__(self):
            self.fieldnames = ['Date of Task', 'Task Name', 'Time Spent', 'Additional Notes']

    def writer(self, date, name, time, notes):
        with open('log.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, lineterminator='\n', fieldnames=self.fieldnames)
            writer.writerow({'Date of Task': date, 'Task Name': name, 'Time Spent': time, 'Additional Notes': notes})
            csvfile.close()

    #  Appends whole row based on date pattern
    @staticmethod
    def reader(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) in row[0]:
                    output.append(row)
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
        return output

    #  Appends whole row based on time spent pattern
    @staticmethod
    def reader4(pattern):
        output = []
        with open('log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if str(pattern) in row[2]:
                    output.append(row)
        return output

    def rinse_repeat(self):
        pass
