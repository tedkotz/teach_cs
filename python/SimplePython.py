#!/usr/bin/env python

import os
import thread
import time
from Tkinter import *

def SimpleClear():
    if 0 != os.system('cls || clear'):
        print('\n' * 100)

#def SimpleDim( x, y=0, z=0 ):
#    if y < 1:
#        return([0]*x)
#    elif z < 1:
#        return([[0]*y]*x)
#    else:
#        return([[[0]*z]*y]*x)


def SimpleDim( *args ):
    def loop( lengths ):
        head, rest = lengths[0], lengths[1:]
        return([0 if rest is () else loop(rest)]*head)
    return loop( args )

BLUE=0
CYAN=0

root=None
canvas=None

def SimpleGr(background=BLUE, border=CYAN):
    global root
    global canvas

    def key(event):
        print "pressed", repr(event.char)

    def callback(event):
        print "clicked at", event.x, event.y
        canvas.focus_set()

    root = Tk()

    canvas = Canvas( root, height=240, width=360, bg="Blue")
    canvas.create_rectangle(65, 35, 135, 65, fill="yellow")
    canvas.pack()

    canvas.bind("<Key>", key)
    canvas.bind("<Button-1>", callback)


    #root.mainloop()

    root.update()

    #thread.start_new_thread( loop, () )
    #loop()


def SimpleGrPlot( x, y, x2 = None, y2 = None):
    pass



# Main Program unit tests for library
if __name__ == "__main__":
    SimpleClear()
    a = SimpleDim( 5 )
    print(a)
    a = SimpleDim( 5, 4 )
    print(a)
    a = SimpleDim( 5, 4, 3 )
    print(a)


    SimpleGr()

    i=10
    while(i>0):
        i=i-1
        time.sleep(1)
        root.update()



