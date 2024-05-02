import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 5000  # Masse du sous marin
cd = 0.25 # coefficient de frottement
T = 2000  # poussé constante des moteurs

# creation d'une trajectoire courbé
def vertical_thrust(t):
    return -1000 * np.sin(t / 200) ** 2   #calcul la poussée verticale
# profondeur du fond
sea_floor_depth = -500  # en metre

# temps
dt = 1  # temps en sec
total_time = 2000  # temps total
times = np.arange(0, total_time, dt)
n_steps = len(times)

# condition de début
x = 0
vx = 0
y = -50
vy = 0

# arrays pour stocker la trajectoire
x_positions = [x]
y_positions = [y]

# Simulation loop en utilisant la méthode Euler
for t in times[:-1]:
    if y < sea_floor_depth:
        vx, vy = 0, 0  # arreter quand il touche le fond
    D = cd * np.sqrt(vx**2 + vy**2) * vx
    ax = (T - D) / m
    ay = vertical_thrust(t) / m
    
    # maj de la vélocité
    vx += ax * dt
    vy += ay * dt
    
    # maj des positions
    x += vx * dt
    y += vy * dt
    
    # stock les positions
    x_positions.append(x)
    y_positions.append(y)
    
    if y < sea_floor_depth:
        break  # fin de la simulation si il touche le fond

# trajectoire
plt.figure(figsize=(10, 5))
plt.plot(x_positions, y_positions, label='Visibly Curved Trajectory of the Nautilus')
plt.xlabel('Distance (m)')
plt.ylabel('Depth (m)')
plt.title('Visibly Curved Trajectory of the Nautilus')
plt.legend()
plt.grid(True)
plt.show()