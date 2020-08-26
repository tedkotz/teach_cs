#!/usr/bin/env python3
""" A more structured version of the Hello World Program

"""

__author__ = "<My Name>"


# Rather than going straight into the instruction we want it to take,  we put
# the instructions inside a block or group of code. And we give that block of
# code a name. In this case that name is betterHelloWorld. It is followed by a
# mandatory set of parenthesis.
#
# a block of code like this is called a FUNCTION. Sometimes referred to as a
# procedure, method, or subroutine.
#
# There are limitations with the name it can not start with a number or contain
# certain special symbols such as :;.,()[]'" or spaces. The lack of spaces in
# names is why we use this mix of upper and lower case to indicate word
# boundaries. This is called CamelCase because the up and down humps in the
# words remind us of a camel's humps.

def betterHelloWorld():
    """ Outputs 'Hello, World!' on the console. """
    # Much as the file has a space for descriptive text so does a function
    # These descriptive headers in python are called DOCSTRINGs and as our
    # functions get more complex they will become more expressive.

    # The line that prints the message is still the same
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
