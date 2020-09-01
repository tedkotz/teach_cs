# teach_cs
Beginner computer science curriculum based on writing simple games in python with SimplePython library

## Overview
With the Pandemic, I was asked for my opion on a curriculum to teach younger children how to program.
I have thought about this topic for a long time so I figured I collect all the information I can in this one place.

The goal is to create an environment similar to the one used to teach BASIC programming in the 1980's. I've always believed all computer science topics
can be presented through the context of video games, not all of which are super fun, but all try tobe somewhat interesting and informative.

## Choosing the language

The language choice needs to be something simple enough to quickly learn and powerful enough to be really useful. Though I love C, I wanted to with a readily
available scripting language. I quickly whittled it down to three choices:

* JavaScript
  * Installed and running everywhere
  * A lot of boiler plate needed to get a basic stdio interface
* Lua
  * A great choice for a real video game focused version of the course
  * No great environment exists
  * Perhaps a few too many tradeoffs made for effciency over usability
* Python
  * Probably the most popular scripting language for small CLI projects
  * The mandatory white space does encourage good coding practices early.

**WINNER: PYTHON**

Really any of these or any other language would probably be great for this. The real focus is the assignment list, that incrementally builds up a toolbox of essential programming skills. Originally the target was 2/3 compatible python, but the peculiar design decisions in python 2 and the even more peculiar choices that the python 3 change pushed on writing compatible code made python 3 the best option.

## Excluded Topics

This is more important than what got in because it is probably the thing people will question the most. This list is not all inclusive, but covers what I thinkk are the most questionable decisions.
#### Object Oriented Programming
It is not that I think students can't hack it. I think it just wastes a lot of time on theory that is better spent later or on a language with an OOP focus like Java. This also allows students to just jump in. Some of this may sneak in with some libraries anyway
#### Functional Programming
More elements of this are likely to show up in the examples than OOP, but not really the focus of this course
#### Higher Complexity Math
One goal of this course is to minimize the complexity of Math involved, but still keep Math there. One example of this is the early focus on input and variables as strings. Which when you think about is actually more inline with how computers actually interact with users.
#### Real Graphics or Widget toolkits
These generally rely heavily on OOP to understand. They introduce a lot of complexity that it overly tied to the specific implementation. For most of the classic BASIC games of this ilk a 360x240 16-color (really 24-bit color) display should be enough.
#### Interupt or Event driven input.
This isn't needed and can create renetance issues that are better left for future.

### Links
https://www.python.org/dev/peps/pep-0257/
https://www.w3schools.com/colors/colors_names.asp
https://www.python.org/dev/peps/pep-0396/
https://numpydoc.readthedocs.io/en/latest/format.html
https://realpython.com/documenting-python-code/
http://www.vintage-basic.net/games.html

## Examples in Lesson Order
1. [Hello World](python/HelloWorld.py)
1. [Better Hello World](python/BetterHelloWorld.py)
1. [Hello You](python/HelloYou.py)
1. There are missing lessons after this point and commetns are sparce
1. [Conversation](python/Conversation.py)
1. [Bouncing Block](python/BouncingBall.py)
1. [Modular Bounce](python/ModularBounce.py)
1. [More Bouncing Blocks](python/MoreBalls.py)
1. [Modular Physics Bounce](python/ModularPhysicsBounce.py)
1. [Particles](python/ParticlesBounce.py)
1. [Paddle](python/Paddle.py)



