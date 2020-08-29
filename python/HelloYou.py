#!/usr/bin/env python3
""" A Hello World like program that uses variable to change who is being greeted

"""

__author__ = "<My Name>"

from SimplePython import SimpleClear


def HelloYou():
    """ Outputs Some Friendly greetings on the console. """

    SimpleClear() # use Simple Python routine to clear the screen

    myVariable = "World" # This line creates a VARIABLE called unoriginally
    # myVariable set to a value of the string "World". Variable names follow
    # similar name limitations as functions can't start with a number, limited
    # use of special characters and no spaces. So once again we can make use of
    # CamelCase to provide more flexibility in names.
    #
    # Variables are how the computer remembers information. Think of it like a
    # box or other container with the variable name on the outside and contents
    # can be switched around. The above line takes the myVariable box and puts
    # the string "World" inside that box.
    # Any time the myVariable box is opened in the future the contents "World"
    # will be inside.

    print ( 'Hello, ' + myVariable + '!' )
    # This print command is fed an expression made by taking the string
    # 'Hello, ', the contents of the variable and the string '!' and
    # CONCATENATES them together. Concatenates is a fancy word for sticking
    # two smaller strings together to make a bigger string. The plus signs
    # in the line above tell python to concatenate these strings together you
    # can kind of thinking about it like adding the strings together.
    # myVariable contains the string "World" thus this is the equivalent of
    # 'Hello, ' + "World" + '!'
    # which concatenates to 'Hello, World!'

    myVariable = "Ted"
    # now this ASSIGNS a different value to myVariable. Imagine it opens the
    # box called myVariable and instead of looking at what is inside it empties
    # it out a puts a new value inside. Setting the variable to my first name
    # now let's see how this changes the behaviour of the print statement.

    print ( 'Hello, ' + myVariable + '!' )
    # same line of code as above, but different result because now myVariable
    # contains my first name so it says hello to me.
    # A little informal if you ask me. Let's see if we can fix that ;)

    myVariable = myVariable + " Kotz"
    # Here we again assign a value to myVariable, but it is the concatenation
    # of the old value of the variable and a new part my lastname.

    print ( 'Hello, ' + myVariable + '!' )
    # Can you figure out what this will print this time?

    # NOTE: variables have a feature called SCOPE. scope is the area of the code
    # over which they can be used. By default variables in python have function
    # scope. This means a variable can only be accessed in the function in which
    # it was created. It also can't be accessed until it is created. So, don't
    # try to print variables before you created them.
    #
    # This does mean that two variables with the same name in two code blocks in
    # different functions are actually treated as different boxes. even though
    # they have the same name their contents could be different.

# so if you tried to access myVariable here. it would not exist so it might
# generate an error or print as None.

if __name__=="__main__":
    HelloYou()

# How would you modify the variable to make it say hello to you?
