#!/usr/bin/env python
""" My first python program

This program demonstrates how to do basic console output, and the essential
parts of a python script.
"""

# <-- Anything after a # character in python is ignored as a comment
# Comments are used to add details explaining a piece of code.

# This first line of the file is a special comnet that tells the computer that
# this file contains a python program and should be treated that way.

# The second part with the triple quotes (""") is a special multi-line
# comment that can be used by the python tools to describe the contents
# of this file.

# This next part can be use to specify information about he who wrote this code
# and how they intend others to use it
__author__ = "<My Name>"
__copyright__ = "Copyright <Year>, <Owner>"
__credits__ = ["<My Name>"]
__license__ = "Public Domain"
__version__ = "0.0.1a"
__maintainer__ = "<My Name>"
__email__ = "<My E-mail>"
__status__ = "Experimental"


# +-print is a function, or command that displays something to the output
# |   +-Functions are commanded to perform their action by following them with
# |   | parenthesis (). The parenthesis contain any inputs that will change how
# |   | the function works.
# |   |
# |   |  +-'Hello, World!' is a string, a type of data used by the computer.
# |   |  |  Data like strings are not commands for the computer, but what they
# |   |  |  work on. A string in python is wrapped in single (') , double ("),
# |   |  |  triple single (''') or triple double quotes (""").
# |   |  |
# |   |  |  Here, the print function is passed input of a string of
# |   |  |  text 'Hello, World!' to output on the screen.
# \/  \/ \/
print ( 'Hello, World!' )


