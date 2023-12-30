import random
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

L = 1         # k/m
h = 10        # k/h
a = 0.02      # this is alpha
meshx = 0.1   # mesh/m
mesht = 0.25  # mesh/h
c = 100       # 100 degree C
r = a * mesht / (meshx**2)
te = np.zeros(((int(h/mesht))+1, int((L/meshx)+1)))  # matris dama(temperture)

j = 0
for x in np.arange(0, L+meshx, meshx):
    te[0, j] = c * math.sin((math.pi * x) / L)
    j = j+1

te[:, 0] = 0                    # force sharayet marzi
te[:, int(L/meshx)] = 0         # force sharayet marzi

for i in np.arange(1, (int(h/mesht))+1):

    tem = np.zeros((2, int((L/meshx))+1))
    for k in np.arange(1, int((L/meshx))):
        tem[0, k] = random.randint(40, 80)

    m = 1
    error = 1
    er = np.zeros((1, int((L/meshx)-1)))

    while error > 0.001:

        for n in np.arange(1, int((L/meshx))):
            tem[1, n] = ((r * (tem[m-1, n+1]+tem[m, n-1])) /
                         (2*r+1)) + (te[i-1, n]/(2*r+1))

        for g in np.arange(0, int((L/meshx))-1):
            er[0, g] = (abs(tem[1, g+1]-tem[0, g+1])) / tem[1, g+1]
        error = np.max(er)

        tem[0, :] = tem[1, :]

    te[i, :] = tem[-1, :]

def plot_2d_space(te):
    space_steps = te.shape[1]
    
    plt.figure(figsize=(10, 6))
    for i in range(te.shape[0]):
        plt.plot(np.arange(0, L+meshx, meshx), te[i, :], label=f'Space Step {i}')

    plt.xlabel('X (m)')
    plt.ylabel('Temperature')
    plt.title('2D Temperature Distribution Over Space')
    plt.legend()
    plt.show()

def plot_2d_time(te):
    time_steps = te.shape[0]
    
    plt.figure(figsize=(10, 6))
    for j in range(te.shape[1]):
        plt.plot(np.arange(0, h+mesht, mesht), te[:, j], label=f'Time Step {j}')

    plt.xlabel('Time (h)')
    plt.ylabel('Temperature')
    plt.title('2D Temperature Distribution Over Time')
    plt.legend()
    plt.show()

def plot_3d(te):
    L, h = te.shape[1], te.shape[0]
    X, Y = np.meshgrid(np.linspace(0, L, L), np.linspace(0, h, h))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, te, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Time')
    ax.set_zlabel('Temperature')
    ax.set_title('3D Temperature Distribution')

    plt.show()

print(te)
plot_2d_space(te)
plot_2d_time(te)
plot_3d(te)