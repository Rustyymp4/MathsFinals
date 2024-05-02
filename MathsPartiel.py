import matplotlib.pyplot as plt
import numpy as np
import math

def phi1(x):
    return (((x - 1)**2) * (2 * x + 1))

def phi2(x):
    return (x**2 * (-2 * x + 3))

def phi3(x): 
    return ((x - 1)**2 * x)

def phi4(x):
    return (x**2 * (x - 1))

def rotation(x, y, angle):
    vector = [0 - x[0], 0 - y[0]]

    for k in range (len(x)):
        x[k] += vector[0]
        y[k] += vector[1]

    if angle == 90:
        rot = [math.cos(math.pi/2), -math.sin(math.pi/2), math.sin(math.pi/2), math.cos(math.pi/2)]

    elif angle == 180:
        rot = [math.cos(math.pi), -math.sin(math.pi), math.sin(math.pi), math.cos(math.pi)]

    elif angle == 270:
        rot = [math.cos(math.pi*1.5), -math.sin(math.pi*1.5), math.sin(math.pi*1.5), math.cos(math.pi*1.5)] 

    xPrime = []
    yPrime = []

    for k in range (len(x)):
        xPrime.append(rot[0] * x[k] + rot[1] * y[k])
        yPrime.append(rot[2] * x[k] + rot[3] * y[k])

    for k in range (len(x)):
        xPrime[k] -= vector[0]
        yPrime[k] -= vector[1]

    return [xPrime, yPrime]

def hermiteModerne(x0, y0, tan0, x1, y1, tan1):
    interval = np.linspace(x0, x1, 50)
    x = []
    y = []

    for i in interval:
        x.append(i)
        phix = (i - x0)/(x1 - x0)
        y.append(y0 * phi1(phix) + y1 * phi2(phix) + (y0 - x0) * tan0 * phi3(phix) + (y0 - x0) * tan1 * phi4(phix))

    return [x,y]

abscisses = []
ordonnees = []

x = [3.6, 8.55, 7.5, 9.35, 9.2, 6, 6, 2, 2, 5.95]
y = [9.6, 8.5, 5.1, 5.5, 3.5, 3, 1.6, 2.6, 7, 7]
t = [2, -1, -1, 0, 1, -1, 0.2, -0.4, 1, 0.5]

for i in range (0, 8):
    listA = []
    listO = []
    C = hermiteModerne(x[i], y[i], t[i], x[i+1], y[i+1], t[i+1])
    for k in range(len(C[0])):
        listA.append(C[0][k])
        listO.append(C[1][k])

    if i in [1, 3, 5]:
        for k in range(len(listA)):
            abscisses.append(rotation(listA, listO, 90)[0][k])
            ordonnees.append(rotation(listA, listO, 90)[1][k])
        

    elif i in [4, 6]:
        for k in range(len(listA)):
            abscisses.append(rotation(listA, listO, 180)[0][k])
            ordonnees.append(rotation(listA, listO, 180)[1][k])

    elif i in [7, 9]:
        for k in range(len(listA)):
            abscisses.append(rotation(listA, listO, 270)[0][k])
            ordonnees.append(rotation(listA, listO, 270)[1][k])

    else :
        for k in range(len(listA)):
            abscisses.append(listA[k])
            ordonnees.append(listO[k])

plt.plot(abscisses, ordonnees)
plt.show()



    
