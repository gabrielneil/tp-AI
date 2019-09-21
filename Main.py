import csv

with open('X_test.csv', 'r') as x_test:
    csv_reader = csv.reader(x_test)

    for line in csv_reader:
        print(line)