#!/usr/bin/env python
##\file testPass.py
#\brief en bref:Programme de tests.
#\author lyase D.
#\version 0.1
#\date 10 Juin 2010.\n
# plus d'info sur le fichier ci present.
## @package testPass.py
# this module is the central repository of our tests.
# each class is a new world.
# each methode is a test in that world.
# think use cases.

import random
import unittest
## this class will hold all the test cases of the app it will act as the test runner\n 
# and doc generator seed.
#each test will be written in a function starting by keywork test \n
# and it's purpose described in embeded doc.
# before the actual code as shown here.

class TestSequenceFunctions(unittest.TestCase):

## the setUp is rerun before each test.
#more doc on setup.
    def setUp(self):

        self.seq = range(10)
#--------------------------------doc of testPass -----------------------------------------

## this method is test is the hello world of tests it will always pass.
    #  @param self The object pointer.
        # make sure the shuffled sequence does not lose any elements

    def testPass(self):

    #  @param self The object pointer.
        # make sure the shuffled sequence does not lose any elements

        self.assertEqual(True,True)
        # define your test as methods before this line and under self.assert# test methods will be here
## this test shows how to add code implemented elsewere (imports) .
    def testimport(self):

        self.assertEqual(a,1)
    #  @param self The object pointer.
        # make sure the shuffled sequence does not lose any elements

if __name__ == '__main__':
    unittest.main()

# test push
