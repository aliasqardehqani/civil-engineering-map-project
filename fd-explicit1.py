import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def explicit(L, h, a, meshx, mesht, c):
    te = np.zeros(((int(h/mesht))+1, int((L/meshx)+1)))  # Temperature matrix

    j = 0
    for x in np.arange(0, L+meshx, meshx):
        te[0, j] = c * math.sin((math.pi * x)/L)
        j += 1

    te[:, 0] = 0                    # Boundary condition
    te[:, int(L/meshx)] = 0         # Boundary condition

    for i in np.arange(1, (int(h/mesht))+1):
        for j in np.arange(1, (int(L/meshx))):
            te[i, j] = ((a*mesht/(meshx**2)) *
                        (te[i-1, j+1]-2*te[i-1, j]+te[i-1, j-1])) + te[i-1, j]

    return te

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

if __name__ == "__main__":
    L = 1         # length/m
    h = 10         # time/h
    a = 0.02       # alpha variable
    meshx = 0.1    # mesh/m
    mesht = 0.25   # mesh/h
    c = 100        # 100 degrees Celsius

    te_result = explicit(L, h, a, meshx, mesht, c)
    print(te_result)

    plot_2d_space(te_result)
    plot_2d_time(te_result)
    plot_3d(te_result)
