#!/usr/bin/env python3
""" My first python program

This program demonstrates how to do basic console output, and the essential
parts of a python script.
"""

__author__ = "<My Name>"

# <-- Anything after a # character in python is ignored as a COMMENT.
# Comments are used to add details explaining a piece of code. They do
# not change what python does because they are ignored by python.
# They are notes for other people who might read the code

# This first line of the file is a special comment that though ignored by python
# tells the computer that this file contains a python program and should be
# treated that way. This is called a HASHBANG or shebang and is used to specify
# the language in use for many different types of programs

# The second part with the triple quotes (""") is a special multi-line
# comment that can be used by the python tools to describe the contents
# of this file.

# This next part can be use to specify information about he who wrote this code
# and how they intend others to use it. This file only has the _author field
# so we can specify who wrote it. This is where you put your name on the
# projects in this series

# Now we get to the real heart of this program. This is the instruction that
# does the task we want the program to do.

# +-print is a FUNCTION, or command that displays something to the output
# |   +-Functions are commanded to perform their action by following them with
# |   | parenthesis (). The parenthesis contain any inputs that will change how
# |   | the function works.
# |   |
# |   |  +-'Hello, World!' is a STRING, a type of data used by the computer.
# |   |  |  Data like strings are not commands for the computer, but what they
# |   |  |  work on. A string in python is wrapped in single (') , double ("),
# |   |  |  triple single (''') or triple double quotes ("""). These allow you
# |   |  |  to use ' or " in a string without confusing when it starts and
# |   |  |  stops.
# |   |  |
# \/  \/ \/
print ( 'Hello, World!' )
# So here, the print function is passed input of a string of text
# 'Hello, World!' to output on the screen.

# Can you write a program the outputs:
# It's time to party

# WATCH OUT 4: the single quote in It's is going to cause problems, if you wrap
# the string in single quotes. What can you use instead?
