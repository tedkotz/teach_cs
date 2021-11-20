#!/usr/bin/env python3
""" """

__author__ = "<My Name>"

from SimplePython import *
from datetime import datetime

def conversation():
    """ """
    SimpleClear()
    print ("Hello, What is your name?")
    name=input(':')
    print ("Hello, "+name+".")
    print ("What year were you born, "+name+"?")
    birthYear = input(':')
    currentYear = datetime.now().strftime('%Y')
    age = int(currentYear) - int(birthYear)
    print( "This year you turn " + str(age) + ", " + name + "." )
    print( "What do you think?" )
    input(":")
    print ("I don't know about that.")
    print ("Goodbye, "+name+".")

if __name__ == "__main__":
    conversation()
