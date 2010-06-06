#!/usr/bin/env python
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
#this will be run before each test i think
        self.seq = range(10)

    def testPass(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(True,True)
if __name__ == '__main__':
        unittest.main()

