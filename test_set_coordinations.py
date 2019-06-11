from create_particles import Particles
from simulation import simulation
import unittest
import numpy as np
import csv
import numpy.ma as ma

class Test_coordinates(unittest.TestCase):
    def setUp(self):
        n =100
        self.xmax = 10
        self.xmin = 0
        self.ymax = 20
        self.ymin = 0
        particles = Particles('nazwa', n)
        self.simulation = simulation(particles)
        self.simulation.set_coordinations(n, self.xmax, self.xmin, self.ymax, self.ymin)

    def test_x(self):
        xarray = self.simulation.particles.coordinates[0]
        test_array = np.where(xarray < self.xmax, xarray, 0)
        test_array2 = np.where(self.xmin <= test_array, test_array, 0)
        #print(test_array2)
        #print(xarray)
        self.assertTrue(np.array_equal(test_array2, self.simulation.particles.coordinates[0]))

    def test_y(self):
        xarray = self.simulation.particles.coordinates[1]
        test_array = np.where(xarray < self.ymax, xarray, 0)
        test_array2 = np.where(self.ymin <= test_array, test_array, 0)
        #print(test_array)
        self.assertTrue(np.array_equal(test_array2, self.simulation.particles.coordinates[1]))


if __name__ == '__main__':
    unittest.main()