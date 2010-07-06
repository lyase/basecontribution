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
