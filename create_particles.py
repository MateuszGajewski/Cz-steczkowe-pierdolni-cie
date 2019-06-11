import numpy as np
import random
import csv
np.set_printoptions(suppress=True)
class Particles():

    def __init__(self, name, number = 2, dimension = 2, datatype = np.float32, mass = 1, radius = 0.1, bounce_dist = 0.01):
        if number < 0:
            raise
        if dimension < 0:
            raise
        self.name  = name
        self.datatype = datatype
        self.number  = number
        self.mass = mass
        self.radius  = radius
        self.dimension = dimension
        self.coordinates = np.zeros((self.dimension, self.number), dtype=self.datatype)
        self.velocities = np.zeros((self.dimension, self.number), dtype=self.datatype)
        self.bounce_dist = bounce_dist
        with open(self.name, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)

        with open(self.name + 'v', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)


    def log(self):
        lists = np.ndarray.tolist(self.coordinates)
        with open(self.name, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            for i in lists:
                #print(i)
                csvwriter.writerow(i)

    def log_v(self):
        lists = np.ndarray.tolist(self.velocities)
        with open(self.name + 'v', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            for i in lists:
                csvwriter.writerow(i)

    def __del__(self):
        pass









