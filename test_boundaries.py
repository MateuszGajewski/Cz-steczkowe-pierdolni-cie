from create_particles import Particles
from simulation import simulation
import unittest
import numpy as np
import csv
import numpy.ma as ma

class Test_coordinates(unittest.TestCase):
    def setUp(self):
        n =100
        self.xmax = 100
        self.xmin = 10
        self.ymax = 200
        self.ymin = 5
        particles = Particles('nazwa', n)
        self.simulation = simulation(particles)
        self.simulation.set_boundaries(self.xmax, self.xmin, self.ymax, self.ymin)

    def test_x(self):
        self.assertEqual(self.simulation.xmax_boundary, self.xmax)
        self.assertEqual(self.simulation.xmin_boundary, self.xmin)
        self.assertEqual(self.simulation.ymax_boundary, self.ymax)
        self.assertEqual(self.simulation.ymin_boundary, self.ymin)


if __name__ == '__main__':
    unittest.main()