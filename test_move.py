from create_particles import Particles
from simulation import simulation
from movment import move_particles
import unittest
import numpy as np
import csv
import numpy.ma as ma

class Test_move_particles(unittest.TestCase):
    def setUp(self):
        self.n =10
        self.vmax = 1
        particles = Particles('nazwa', self.n)
        self.simulation = simulation(particles)
        self.simulation.set_velocities(self.n, self.vmax)
        self.xmax = 10
        self.xmin = 0
        self.ymax = 20
        self.ymin = 0
        self.simulation.set_coordinations(self.n, self.xmax, self.xmin, self.ymax, self.ymin)

    def test_x(self):
        x_1 = self.simulation.particles.coordinates[0] + self.simulation.particles.velocities[0]
        print(x_1, self.simulation.particles.velocities[0])
        print(self.simulation.particles.coordinates[0])
        self.simulation.run(2, 1)
        print(self.simulation.particles.coordinates[0])
        self.assertEqual(x_1, self.simulation.particles.coordinates[0])

    def test(self):
        x_1 = self.simulation.particles.coordinates + self.simulation.particles.velocities
        print(x_1, self.simulation.particles.velocities)
        print(self.simulation.particles.coordinates)
        self.simulation.run(1, 1)
        print(self.simulation.particles.coordinates)
        self.assertTrue(np.array_equal(x_1, self.simulation.particles.coordinates))




if __name__ == '__main__':
    unittest.main()