from create_particles import Particles
import unittest
import numpy as np
import csv

class Test_Particles(unittest.TestCase):
    def setUp(self):
        self.n = 100
        self.kulki = Particles('nazwa', self.n)
    def test_coordinates(self):
        self.assertEqual(self.kulki.coordinates.shape,(2, self.n) )

    def test_coordinates(self):
        self.assertEqual(self.kulki.velocities.shape,(2, self.n) )

    def test_log(self):
        self.kulki.log()
        self.kulki.log()
        with open(self.kulki.name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            row_count = 0
            for row in csvreader:
                #print (row)
                row_count+=1
                column_count = len(row)

        self.assertEqual(row_count, int(4))
        self.assertEqual(column_count, self.n)




if __name__ == '__main__':
    unittest.main()
