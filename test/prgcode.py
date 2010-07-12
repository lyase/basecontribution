#!/usr/bin/env python
##\file prgcode.py
#\brief en bref:Programme de demo.
#\author lyase D.
#\version 0.1
#\date 10 Juin 2010.\n

## function that reports true can be use to check if the module is loaded.
def module_loaded():

    return True;
## this class defines a simple object .
# with just one method .


class myobj:
  ## this is the only method of my object  .
# it will return a string with "myobj" .

  def name(self):
    return "myobj"
    ## this class defines a simple object derived from myobj .
# with no method just the inherited.

class derivedmyobj(myobj):
  def derivedname(self):
    return "derivedmyobj"
    ## this class defines a simple object that wll be a singleton in the application.
# there will be only one instance of MyClass  or any class using
#     __metaclass__ = Singleton in its definition
# be carefull i am not sure how this really works
class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None
 
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
 
        return cls.instance

# Utilisation
## this class  will be a singleton in the application.
class MyClass(object):
    __metaclass__ = Singleton
 
## testimport shows how to document a python function using Latex in the documentation.
# Here is an example of inserting a mathematical formula into the documentation  :
#   \f[
#   V(t,x)=\inf_{(\alpha_s)_s}
#   I\!\! E_{t,x}
#   \left\{\Psi\left(X_\tau\right)
#   \right\}
#   \f]
# just in case it is the returned value of this function \n 
# note that all formulas must be valid LaTeX math-mode commands.\n
#this function was written and documented  on:\date june 18 2010
def LatexDemoDoc():
    aLatex_var=1