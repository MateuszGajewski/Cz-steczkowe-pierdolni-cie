import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

import csv
import pandas as pd
from create_particles import Particles
from simulation import simulation
from movment import move_particles
np.set_printoptions(suppress=True)


class Animation():
    def __init__(self):
        self.W =200

        self.n = 400
        self.vmax = self.W/(2*self.n)
        particles = Particles('symulacja', self.n)
        self.simulation = simulation(particles)
        self.simulation.set_velocities(self.n, self.vmax)
        self.xmax = 30
        self.xmin = 0
        self.ymax = 30
        self.ymin = 0
        self.simulation.set_coordinations(self.n, 1, self.xmin, self.ymax, self.ymin)
        self.simulation.set_boundaries(self.xmax, self.xmin, self.ymax, self.ymin)
        self.simulation.run(2000, 0.5)#(1/(self.W))*np.log2(self.W))
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
        self.points, = ax.plot([], [], 'bo')

        ax.set_ylim(self.ymin, self.ymax)
        ax.set_xlim(self.xmin, self.xmax)

        pl = plot(self)


        ani = animation.FuncAnimation(fig, pl.animate, interval=10)
        plt.show()
        ani.save('symulacja5.mp4', fps=50)

    def plot_test(self):
        csvfile = pd.read_csv('nazwa', header=0, nrows=5000, skiprows=0, delimiter=",")
        print(csvfile)
        csvfile1 = pd.read_csv('nazwa', header=0, nrows=5000, skiprows=1, delimiter=",")
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

class plot():
    def __init__(self, name):

        self.csvfile = open('symulacja', 'r')
        self.plots = csv.reader(self.csvfile, delimiter=',')
        self.name = name
    def animate(self,i):
        x = []
        row = self.plots.__next__()
        for i in row:
            x.append(float(i))
        y = []
        row = self.plots.__next__()
        for i in row:
            y.append(float(i))
        #print(x,y)
        self.name.points.set_data(x, y)
if __name__ == '__main__':
    ani = Animation()
    ani.plot()