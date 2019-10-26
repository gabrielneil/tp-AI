import csv
import random

import numpy as np

# vars definition
x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = 1

Sample0 = []
Sample1 = []
Sample2 = []
Sample3 = []
Sample4 = []
Sample5 = 1

y = []
w = []
u = []
finalU = []
errors = []
finalErrors = []
deltaW = []
yAux = []
learningRate = 0.04

level = 0
salidaTrain1 = []
salidaTrain0 = []
salidaFinal1 = []
salidaFinal0 = []

errorCuadraticoFinal = float(0.5)
# csv files reference
with open('X_train.csv', 'r') as x_train, open('Y_train.csv', 'r') as y_train, open('X_test.csv') as x_test:
    csv_x_train = csv.reader(x_train)
    csv_y_train = csv.reader(y_train)
    csv_x_test = csv.reader(x_test)

    # loading X arrays
    for line in csv_x_train:
        x0.append(line[0])
        x1.append(line[1])
        x2.append(line[2])
        x3.append(line[3])
        x4.append(line[4])

        # loading Y array
    for line in csv_y_train:
        yAux.append(line)

    for line in csv_x_test:
        Sample0.append(line[0])
        Sample1.append(line[1])
        Sample2.append(line[2])
        Sample3.append(line[3])
        Sample4.append(line[4])

y = np.array(yAux)
# init random weights
for x in range(6):
    w.append(random.random())


def getCuadraticerror(levels):
    return float((1 / (levels * 2)) * getErrorsSum())


def getErrorsSum():
    res = float(0)
    for error in errors:
        res += (error * error)
    return res


# trainning
def train(errorCuadratico):
    level = 0
    while errorCuadratico > 0.2:
        for x in range(x0.__len__()):
            oK = (float(x0[x]) * float(w[0])) + (float(x1[x]) * float(w[1])) + (float(x2[x]) * float(w[2])) + (
                    float(x3[x]) * float(w[3])) + (float(x4[x]) * float(w[4]) + (float(w[5])))
            # u list
            u.append(oK)
            error = float(y[x]) - oK
            # error list
            errors.append(error)
            # learning rate * error
            preDeltaW = (learningRate * error)
            preDeltaWArray = [(preDeltaW * w[0]), (preDeltaW * w[1]), (preDeltaW * w[2]), (preDeltaW * w[3]),
                              (preDeltaW * w[4]), preDeltaW * w[5]]
            # update weights
            w[0] += preDeltaWArray[0]
            w[1] += preDeltaWArray[1]
            w[2] += preDeltaWArray[2]
            w[3] += preDeltaWArray[3]
            w[4] += preDeltaWArray[4]
            w[5] += preDeltaWArray[5]

            if oK >= 0.5:
                salidaTrain1.append(oK)
            else:
                salidaTrain0.append(oK)
            level += 1
        errorCuadratico = getCuadraticerror(level)
    return errorCuadratico


# clasificador
def sort():
    for x in range(Sample0.__len__()):
        nextU = (float(Sample0[x]) * float(w[0])) + (float(Sample1[x]) * float(w[1])) + (
                float(Sample2[x]) * float(w[2])) + (float(Sample3[x]) * float(w[3])) + \
                (float(Sample4[x]) * float(w[4]) + (float(w[5])))

        finalU.append(nextU)
        if nextU >= 0.5:
            salidaFinal1.append(nextU)
        else:
            salidaFinal0.append(nextU)


errorCuadraticoFinal = train(errorCuadraticoFinal)
sort()
print("-------------Entenando---------------")
print("Tasa de aprendizaje: " + learningRate.__str__())
print("Cantiad de elementos clasificados en 1: " + salidaTrain1.__len__().__str__())
print("Cantiad de elementos clasificados en 0: " + salidaTrain0.__len__().__str__())
print("error cuadratico: " + errorCuadraticoFinal.__str__())
print("Vector Pesos W " + w.__str__())
print("Vector U de Entrenamiento:" + u.__str__() + "\n")
print("-------------Clasificador-----------------")
print("Vector U Final: " + finalU.__str__())
print("Cantiad de elementos grupo en 1: " + salidaFinal1.__len__().__str__())
print("Cantiad de elementos grupo en 0: " + salidaFinal0.__len__().__str__())
