#!/usr/bin/env python3
""" A more structured version of the Hello World Program

"""

from SimplePython import SimpleClear  # This line gives this program access to
# additional functionality by importing a new function called SimpleClear from
# from a MODULE called SimplePython. Modules are a file or set of files that
# contain additional software to provide extended functionality.
#
# This module SimplePython was written to go with this course in order to
# provide some simple commands to let the course focus on helping you get solid
# base skills. the file is included with the examples here for review. Though
# a lot of what it does might not make sense until you get more experience with
# python.


__author__ = "<My Name>"


# Rather than going straight into the instructions for organization,  we put
# the instructions inside a block or group of code. And we give that block of
# code a name. In this case that name is betterHelloWorld. It is followed by a
# mandatory set of parenthesis.
#
# A block of code like this is called a function. Sometimes referred to as a
# procedure, method, or subroutine. Similar to print, but we can define our own.
#
# There are limitations with the name. It can not start with a number or contain
# certain special symbols such as :;.,()[]'" or spaces. The lack of spaces in
# names is why we use this mix of upper and lower case to indicate word
# boundaries. This is called CamelCase because the up and down humps in the
# words remind us of a camel's humps.

def betterHelloWorld():
    """ Outputs 'Hello, World!' on the console. """
    # Much as the file has a space for descriptive text so does a function
    # These descriptive headers in python are called DOCSTRINGs and as our
    # functions get more complex they will become more expressive.

    SimpleClear() # Command from SimplePython to clear the screen
    # Sometimes it is nice to clear the screen at the start of a program to
    # remove any distractions or just neaten up the initial display.

    # The line that prints the message is still the same from HelloWorld
    print ( 'Hello, World!' )

    #                 ^
    #                 |
    # Note the colon above after betterHelloWorld() that indicates the start of
    # the block of instructions. All the line of code indented after that are
    # part of that block of code and considered part of it.
    # Any other line indented like these comments would be part of the block
    # and part of betterHelloWorld


# A line not indented is not part of the block and indicates that the block has
# ended. Indenting a later line will not make it part of that instruction block.


# This final block specifies where to start execution when this program is run
# in this case we start in the betterHelloWorld block defined above
if __name__=="__main__":
    betterHelloWorld()
