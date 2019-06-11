from create_particles import Particles
from simulation import simulation
import unittest
import numpy as np
import csv
import numpy.ma as ma

class Test_velocitiess(unittest.TestCase):
    def setUp(self):
        self.n =100
        self.vmax = 10
        particles = Particles('nazwa', self.n)
        self.simulation = simulation(particles)
        self.simulation.set_velocities(self.n, self.vmax)
    def test_max_velocity_x(self):
        varray = self.simulation.particles.velocities[0]
        test_varray = np.where(varray<=self.vmax, varray, 0)
        test_varray2 = np.where((-1)*self.vmax <= test_varray, test_varray, 0)
        self.assertTrue(np.array_equal(test_varray2, self.simulation.particles.velocities[0]))

    def test_max_velocity_x(self):
        varray = self.simulation.particles.velocities[1]
        test_varray = np.where(varray <= self.vmax, varray, 0)
        test_varray2 = np.where((-1) * self.vmax <= test_varray, test_varray, 0)
        self.assertTrue(np.array_equal(test_varray2, self.simulation.particles.velocities[1]))

    def test_velocities_x_y(self):
        varray = (self.simulation.particles.velocities[1])**2 + (self.simulation.particles.velocities[0])**2
        test_array = np.where(varray<= (self.vmax)**2, varray, None)

        self.assertTrue(test_array.shape, self.n)




if __name__ == '__main__':
    unittest.main()