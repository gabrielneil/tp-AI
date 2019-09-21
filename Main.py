import csv
import random

with open('X_train.csv', 'r') as x_train:
    csv_x_train = csv.reader(x_train)

    for line in csv_x_train :
        x0 = line[0]
        x1 = line[1]
        x2 = line[2]
        x3 = line[3]
        x4 = line[4]

with open('Y_train.csv', 'r') as y_train:
    csv_y_train = csv.reader(y_train)
    for line in csv_y_train:
        y0 = line

for x in range(5):
    w0 = random.random()
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    w4 = random.random()