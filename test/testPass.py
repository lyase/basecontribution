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
        # define your test as methods before this line and under self.assert
# test methods will be here
## this function does nothing but has fancy documentation on how to write a formula in doc:
# more latex here:
#   \f[
#   V(t,x)=\inf_{(\alpha_s)_s}
#   I\!\! E_{t,x}
#   \left\{\Psi\left(X_\tau\right)
#   \right\}
#   \f]


# just in case it is the returned value of this function \n 
# note that all formulas must be valid LaTeX math-mode commands.\n
#this function was written and documented  on:\date june 18 2010

    def testFakeForLATEXDoc(self):

        self.assertEqual(True,True)

## testimport shows how to add code implemented elsewere (imports)so the code of the application is kept in its proper place imported and used as needed.
# more comments
    def testimport(self):
        import prgcode
        a=prgcode.module_loaded()
        self.assertEqual(a,True)

## testimport_light shows how to add code implemented elsewere (imports)\n
#so the code of the application is kept in its proper place imported and used as needed. this version is light\n as the usage of the function does not require source name but heavier on the import
    def testimport_light(self):
        from prgcode import module_loaded
        a=module_loaded()
        self.assertEqual(a,True)

if __name__ == '__main__':
    unittest.main()

# test push
