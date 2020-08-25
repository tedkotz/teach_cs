#!/usr/bin/env python3

from SimplePython import *
from datetime import datetime

__author__ = "<My Name>"

SimpleClear()
print ("Hello, What is your name?")
name=input(':')
print ("Hello, "+name+".")
print ("What year were you born, "+name+"?")
birthYear = input(':')
currentYear = datetime.now().strftime('%Y')
Age = int(currentYear) - int(birthYear)
print( "This year you turn " + str(Age) + ", " + name + "." )
print( "What do you think?" )
input(":")
print ("I don't know about that.")
print ("Goodbye, "+name+".")
