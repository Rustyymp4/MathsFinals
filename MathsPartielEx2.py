import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button, TextBox

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cursorRange = 0.3
fig, sp = plt.subplots()

x0box = fig.add_axes([0.1, 0.05, 0.1, 0.075])
text_x0box = TextBox(x0box, "X0", textalignment="center")
y0box = fig.add_axes([0.25, 0.05, 0.1, 0.075])
text_y0box = TextBox(y0box, "Y0", textalignment="center")
t0box = fig.add_axes([0.4, 0.05, 0.1, 0.075])
text_t0box = TextBox(t0box, "T0", textalignment="center")

x1box = fig.add_axes([0.55, 0.05, 0.1, 0.075])
text_x1box = TextBox(x1box, "X1", textalignment="center")
y1box = fig.add_axes([0.7, 0.05, 0.1, 0.075])
text_y1box = TextBox(y1box, "Y1", textalignment="center")
t1box = fig.add_axes([0.85, 0.05, 0.1, 0.075])
text_t1box = TextBox(t1box, "T1", textalignment="center")

x2box = fig.add_axes([0.1, 0.15, 0.1, 0.075])
text_x2box = TextBox(x2box, "X2", textalignment="center")
y2box = fig.add_axes([0.25, 0.15, 0.1, 0.075])
text_y2box = TextBox(y2box, "Y2", textalignment="center")
t2box = fig.add_axes([0.4, 0.15, 0.1, 0.075])
text_t2box = TextBox(t2box, "T2", textalignment="center")

x3box = fig.add_axes([0.55, 0.15, 0.1, 0.075])
text_x3box = TextBox(x3box, "X3", textalignment="center")
y3box = fig.add_axes([0.7, 0.15, 0.1, 0.075])
text_y3box = TextBox(y3box, "Y3", textalignment="center")
t3box = fig.add_axes([0.85, 0.15, 0.1, 0.075])
text_t3box = TextBox(t3box, "T3", textalignment="center")

x4box = fig.add_axes([0.1, 0.25, 0.1, 0.075])
text_x4box = TextBox(x4box, "X4", textalignment="center")
y4box = fig.add_axes([0.25, 0.25, 0.1, 0.075])
text_y4box = TextBox(y4box, "Y4", textalignment="center")
t4box = fig.add_axes([0.4, 0.25, 0.1, 0.075])
text_t4box = TextBox(t4box, "T4", textalignment="center")

x5box = fig.add_axes([0.55, 0.25, 0.1, 0.075])
text_x5box = TextBox(x5box, "X5", textalignment="center")
y5box = fig.add_axes([0.7, 0.25, 0.1, 0.075])
text_y5box = TextBox(y5box, "Y5", textalignment="center")
t5box = fig.add_axes([0.85, 0.25, 0.1, 0.075])
text_t5box = TextBox(t5box, "T5", textalignment="center")

x6box = fig.add_axes([0.1, 0.35, 0.1, 0.075])
text_x6box = TextBox(x6box, "X6", textalignment="center")
y6box = fig.add_axes([0.25, 0.35, 0.1, 0.075])
text_y6box = TextBox(y6box, "Y6", textalignment="center")
t6box = fig.add_axes([0.4, 0.35, 0.1, 0.075])
text_t6box = TextBox(t6box, "T6", textalignment="center")

x7box = fig.add_axes([0.55, 0.35, 0.1, 0.075])
text_x7box = TextBox(x7box, "X7", textalignment="center")
y7box = fig.add_axes([0.7, 0.35, 0.1, 0.075])
text_y7box = TextBox(y7box, "Y7", textalignment="center")
t7box = fig.add_axes([0.85, 0.35, 0.1, 0.075])
text_t7box = TextBox(t7box, "T7", textalignment="center")

x8box = fig.add_axes([0.1, 0.45, 0.1, 0.075])
text_x8box = TextBox(x8box, "X8", textalignment="center")
y8box = fig.add_axes([0.25, 0.45, 0.1, 0.075])
text_y8box = TextBox(y8box, "Y8", textalignment="center")
t8box = fig.add_axes([0.4, 0.45, 0.1, 0.075])
text_t8box = TextBox(t8box, "T8", textalignment="center")

x9box = fig.add_axes([0.55, 0.45, 0.1, 0.075])
text_x9box = TextBox(x9box, "X9", textalignment="center")
y9box = fig.add_axes([0.7, 0.45, 0.1, 0.075])
text_y9box = TextBox(y9box, "Y9", textalignment="center")
t9box = fig.add_axes([0.85, 0.45, 0.1, 0.075])
text_t9box = TextBox(t9box, "T9", textalignment="center")

def chooseCoords():

    fig.subplots_adjust(bottom=0.8)
    sp.cla()
    sp.grid(False)
    sp.axis('equal')
    plt.show()

def Submit(event):

    x[0] = float(text_x0box.text)
    y[0] = float(text_y0box.text)
    t[0] = float(text_t0box.text)

    x[1] = float(text_x1box.text)
    y[1] = float(text_y1box.text)
    t[1] = float(text_t1box.text)

    x[2] = float(text_x2box.text)
    y[2] = float(text_y2box.text)
    t[2] = float(text_t2box.text)

    x[3] = float(text_x3box.text)
    y[3] = float(text_y3box.text)
    t[3] = float(text_t3box.text)

    x[4] = float(text_x4box.text)
    y[4] = float(text_y4box.text)
    t[4] = float(text_t4box.text)

    x[5] = float(text_x5box.text)
    y[5] = float(text_y5box.text)
    t[5] = float(text_t5box.text)

    x[6] = float(text_x6box.text)
    y[6] = float(text_y6box.text)
    t[6] = float(text_t6box.text)

    x[7] = float(text_x7box.text)
    y[7] = float(text_y7box.text)
    t[7] = float(text_t7box.text)

    x[8] = float(text_x8box.text)
    y[8] = float(text_y8box.text)
    t[8] = float(text_t8box.text)

    x[9] = float(text_x9box.text)
    y[9] = float(text_y9box.text)
    t[9] = float(text_t9box.text)

    plt.close()
    start()


# Submit button
bbox = fig.add_axes([0.47, 0.55, 0.1, 0.075])
bsubmit = Button(bbox,"Submit")
bsubmit.on_clicked(Submit)

def phi1(x):
    return (((x - 1)**2) * (2 * x + 1))

def phi2(x):
    return (x**2 * (-2 * x + 3))

def phi3(x): 
    return ((x - 1)**2 * x)

def phi4(x):
    return (x**2 * (x - 1))

def rotation(x, y, angle):
    vector = [0 - x, 0 - y]
    x += vector[0]
    y += vector[1]

    if angle == 90:
        rot = [math.cos(math.pi/2), -math.sin(math.pi/2), 
        math.sin(math.pi/2), math.cos(math.pi/2)]

    elif angle == 180:
        rot = [math.cos(math.pi), -math.sin(math.pi), math.sin(math.pi), math.cos(math.pi)]

    elif angle == 270:
        rot = [math.cos(math.pi*1.5), -math.sin(math.pi*1.5), math.sin(math.pi*1.5), math.cos(math.pi*1.5)] 

    xPrime = 0
    yPrime = 0

    xPrime = rot[0] * x + rot[1] * y
    yPrime = rot[2] * x + rot[3] * y

    xPrime -= vector[0]
    yPrime -= vector[1]

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



def start():

    fig.subplots_adjust(bottom=0.8)
    abscisses = []
    ordonnees = []

    plt.plot(x, y,  label="Le trace sans Hermite")

    for i in range (0, 9):
        plt.scatter(x[i], y[i], color='red')
        if x[i] > x[i+1]:
            C = hermiteModerne(x[i+1], y[i+1], t[i+1], x[i], y[i], t[i])
            print(len(C[0]))
            for k in range(len(C[0])):
                abscisses.append(C[0][len(C[0]) - 1 - k])
                ordonnees.append(C[1][len(C[1]) - 1 - k])
        
        else:
            C = hermiteModerne(x[i], y[i], t[i], x[i+1], y[i+1], t[i+1])
            for k in range(len(C[0])):
                abscisses.append(C[0][k])
                ordonnees.append(C[1][k])

    if x[9] > x[0]:
        C = hermiteModerne(x[0], y[0], t[0], x[9], y[9], t[9])
        plt.scatter(x[9], y[9], color='red')
        for k in range(len(C[0])):
            abscisses.append(C[0][len(C[0]) - 1 - k])
            ordonnees.append(C[1][len(C[1]) - 1 - k])

    else:
        C = hermiteModerne(x[9], y[9], t[9], x[0], y[0], t[0])
        plt.scatter(x[9], y[9], color='red')
        for k in range(len(C[0])):
            abscisses.append(C[0][k])
            ordonnees.append(C[1][k])

    plt.plot(abscisses, ordonnees, label="Le trace avec Hermite")
    plt.xlabel("Position X")
    plt.ylabel("Position Y")
    plt.title("Le graph de la Map")
    plt.legend()
    plt.grid(True)
    plt.show()
    
chooseCoords()