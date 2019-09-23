import csv
import random

x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
y = []
w = []

with open('X_train.csv', 'r') as x_train, open('Y_train.csv', 'r') as y_train:
    csv_x_train = csv.reader(x_train)
    csv_y_train = csv.reader(y_train)

    for line in csv_x_train:
        x0.append(line[0])
        x1.append(line[1])
        x2.append(line[2])
        x3.append(line[3])
        x4.append(line[4])

        for line in csv_y_train:
            y.append(line)

for x in range(5):
    w.append(random.random())