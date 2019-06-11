import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

import csv
import pandas as pd
from create_particles import Particles
from simulation import simulation
from movment import move_particles
np.set_printoptions(suppress=True)


class Animation():
    def __init__(self):
        self.W =30

        self.n = 100
        self.vmax = self.W/(2*self.n)
        particles = Particles('symulacja', self.n)
        self.simulation = simulation(particles)
        self.simulation.set_velocities(self.n, self.vmax)
        self.xmax = 50
        self.xmin = 0
        self.ymax = 50
        self.ymin = 0
        self.simulation.set_coordinations(self.n, 10, self.xmin, self.ymax, self.ymin)
        self.simulation.set_boundaries(self.xmax, self.xmin, self.ymax, self.ymin)
        self.simulation.run(200, 0.1)#(1/(self.W))*np.log2(self.W))
    def plot(self):
        fig, ax = plt.subplots()
        csvfile = pd.read_csv('symulacja', header=0, nrows=2, skiprows=0)
        print(csvfile)
        csvfile1 = pd.read_csv('symulacja', header=0, nrows=2, skiprows=1)
        print(csvfile)
        x =[]
        y =[]
        for i in csvfile:
            x.append(float(i))
        for i in csvfile1:
            y.append(float(i))
        print(x, y)
        points, = ax.plot([], [], 'bo')

        ax.set_ylim(self.ymin, self.ymax)
        ax.set_xlim(self.xmin, self.xmax)

        def update(data):

            x = data[0]
            y = data[1]

            points.set_data(x, y)

            return points,

        def generate_points():

            j = 2
            x = []
            y = []
            while True:
                print(j)
                x = []
                y = []
                csvfile = pd.read_csv('symulacja', header=0, nrows=10, skiprows=j, dtype="float32", delimiter=",")
                for i in csvfile:
                    #print(i)
                    x.append(float(i))

                j += 1
                csvfile = pd.read_csv('symulacja', header=0, nrows=10, skiprows=j, delimiter=",")
                for i in csvfile:
                    y.append(float(i))
                yield [x,y]

                j+=1



        ani = animation.FuncAnimation(fig, update, generate_points, interval=100, blit=True)
        #plt.show()
        ani.save('symulacja4.gif', writer='imagemagick', fps=50)


    def plot_test(self):
        csvfile = pd.read_csv('nazwa', header=0, nrows=2, skiprows=0, delimiter=",")
        print(csvfile)
        csvfile1 = pd.read_csv('nazwa', header=0, nrows=2, skiprows=1, delimiter=",")
        print(csvfile)
        x = []
        y = []
        for i in csvfile:
            print(i)
            x.append(float(i))
        for i in csvfile1:
            y.append(float(i))

        print(x)
        print(y)
        plt.scatter(x,y)
        plt.show()

if __name__ == '__main__':
    ani = Animation()
    ani.plot()