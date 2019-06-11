import numpy as np
import simulation
import scipy.spatial.distance as dist
from scipy.spatial.distance import squareform
np.set_printoptions(suppress=True)
import numpy.ma as ma

class move_particles():
    def __init__(self, simulation):

        self.simulation = simulation
        self.v = simulation.particles.velocities
        self.x = simulation.particles.coordinates
        self.r = simulation.particles.radius
    def do_step(self, dt):

        x = self.x
        v = self.v

        bounce_x_right = np.where(np.logical_and(
            self.simulation.xmax_boundary - self.simulation.particles.radius * self.simulation.particles.bounce_dist < x[0], v[0] > 0))
        bounce_x_left = np.where(np.logical_and(
            self.simulation.xmin_boundary + self.simulation.particles.radius * self.simulation.particles.bounce_dist > x[0], v[0] < 0))
        self.bounce(bounce_x_right, 0)
        self.bounce(bounce_x_left, 0)

        bounce_y_right = np.where(np.logical_and(
            self.simulation.ymax_boundary - self.simulation.particles.radius * self.simulation.particles.bounce_dist <
            x[1], v[1] > 0))
        bounce_y_left = np.where(np.logical_and(
            self.simulation.ymin_boundary + self.simulation.particles.radius * self.simulation.particles.bounce_dist >
            x[1], v[1] < 0))
        self.bounce(bounce_y_right, 1)
        self.bounce(bounce_y_left, 1)


        self.colision()


        self.move(dt)
    def bounce(self, array, a):
        self.v[a][array] *= (-1)


    def colision(self):
        distances = dist.squareform(dist.pdist(np.transpose(self.x), 'euclidean'))
        colide = np.where(np.logical_and(distances<self.r * self.simulation.particles.bounce_dist, 0<distances))
        #print()
        #print(self.r * self.simulation.particles.bounce_dist)
        #print(distances)
        #print(colide)
        #print(self.v[:, colide[0]])
        self.v [:, colide[0]] = (self.v[:, colide[0]] * np.flipud(np.absolute(self.x[:,colide[0]]) - self.x[:, colide[1]])/distances[colide[0], colide[1]]) +\
                             (self.v[:, colide[1]] * (np.absolute(self.x[:, colide[0]]) - self.x[:, colide[1]]) / distances[colide[0], colide[1]])
        #print(self.v[:, colide[0]])

    def move(self, dt):

        self.x += self.v*dt


