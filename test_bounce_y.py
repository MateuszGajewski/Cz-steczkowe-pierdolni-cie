from create_particles import Particles
import unittest
import numpy as np
import csv
from animate import Animation
import pandas as pd
from create_particles import Particles
from simulation import simulation
from movment import move_particles

class Test_Particles(unittest.TestCase):
    def setUp(self):
        self.animation = Animation()
        self.animation.n = 2
        self.animation.vmax = 3
        particles = Particles('symulacja', self.animation.n)
        self.animation.simulation = simulation(particles)
        self.animation.simulation.set_velocities(self.animation.n, self.animation.vmax)
        self.animation.xmax = 30
        self.animation.xmin = 0
        self.animation.ymax = 20
        self.animation.ymin = 0
        self.animation.simulation.set_coordinations(self.animation.n, 1, self.animation.xmin, self.animation.ymax, self.animation.ymin)
        self.animation.simulation.set_boundaries(self.animation.xmax, self.animation.xmin, self.animation.ymax, self.animation.ymin)




    def test_coordinate_y(self):
        self.animation.simulation.particles.coordinates = np.zeros((2, 2))
        self.animation.simulation.particles.coordinates[0,0] = 2
        self.animation.simulation.particles.coordinates[0,1] = 2
        self.animation.simulation.particles.coordinates[1,0] = 19
        self.animation.simulation.particles.coordinates[1,1] = 17

        self.animation.simulation.particles.velocities = np.zeros((2, 2))
        self.animation.simulation.particles.velocities[1, 0] = -0.1
        self.animation.simulation.particles.velocities[1, 1] = 0.1
        #print(self.animation.simulation.particles.velocities)
        #print(self.animation.simulation.particles.coordinates)
        #print(self.animation.simulation.particles.coordinates+ self.animation.simulation.particles.velocities*1)

        self.animation.simulation.run(30, 1)

        self.assertEqual(self.animation.simulation.particles.velocities[1, 0], float(0.1))
        self.assertEqual(self.animation.simulation.particles.velocities[1, 1], float(-0.1))




if __name__ == '__main__':
    unittest.main()
