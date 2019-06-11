import numpy as np
import random
class simulation():
    def __init__(self, particles):
        self.particles = particles

    def set_coordinations(self, n, xmax, xmin, ymax, ymin):
        C = self.particles.coordinates
        x = np.random.rand(n)
        y = np.random.rand(n)
        index  = np.arange(n)
        #print(C)
        #print(C[0])
        C[0] = x*xmax - xmin
        C[1] = y*ymax - ymin
    def set_velocities(self, n, vmax):
        V = self.particles.velocities
        alpha = np.random.rand(n) * 2.0 * np.pi
        V[0] = vmax * np.sin(alpha)
        V[1] = vmax * np.cos(alpha)
    def set_boundaries(self, xmax, xmin, ymax, ymin):
        self.xmax_boundary = xmax
        self.xmin_boundary = xmin
        self.ymax_boundary = ymax
        self.ymin_boundary = ymin


