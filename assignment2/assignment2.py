import csv
# Task 2: Read a CSV File

def read_employees():
    dict = {}
    rows = []
    try:
        with open('csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" in dict:
                    rows.append(row)
                else:
                    dict["fields"] = []
    except Exception as e:
        print(e)
    dict['rows'] = rows
    return dict

employees = read_employees()

print(employees)