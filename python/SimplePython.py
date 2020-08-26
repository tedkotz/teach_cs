#!/usr/bin/env python
""" """

import os
from tkinter import *

COLORS = ['BLACK', 'BROWN', 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'VIOLET', 'GRAY', 'WHITE', 'CYAN', 'MAGENTA', 'LIGHTGRAY', 'DIMGRAY', 'TAN', 'INDIGO']

try:
    from matplotlib.colors import is_color_like, get_named_colors_mapping
except ImportError:
    import re
    def is_color_like( value ):
        try:
            value = value.upper()
            if re.compile(r"^#[0-9A-F]{6}$").match(value):
                return True
            elif value in COLORS:
                return True
        except:
            pass
        return False




# This next part can be use to specify information about he who wrote this code
# and how they intend others to use it
__author__ = "<My Name>"
__copyright__ = "Copyright 2020, <Owner>"
__credits__ = ["<My Name>"]
__license__ = "Public Domain"
__version__ = "0.0.1a"
__maintainer__ = "<My Name>"
__email__ = "<My E-mail>"
__status__ = "Experimental"

def SimpleClear():
    """Clears screen."""
    if 0 != os.system('cls || clear'):
        print('\n' * 100)

def SimpleBeep():
    """Makes computer beep"""
    sys.stdout.write('\a')
    sys.stdout.flush()


def SimpleDim( *args ):
    """Returns multidimentional list of zeros"""
    def loop( lengths ):
        head, rest = lengths[0], lengths[1:]
        return([0 if rest is () else loop(rest)]*head)
    return loop( args )

# User Addressable Width of Graphics Mode Display
WIDTH=360
# User Addressable Height of Graphics Mode Display
HEIGHT=240

root=None
canvas=None
frame=None
images=None
fg_color=None
scale=None
image_on_canvas=None
eventQueue=None

def SimpleGrClose():
    """Closes and cleans up Graphics Mode"""
    global root
    global canvas
    global fg_color
    global scale
    global frame
    global images
    global image_on_canvas
    global eventQueue
    if root is not None:
        root.destroy()
    root=None
    canvas=None
    fg_color=None
    scale=None
    frame=None
    images=None
    image_on_canvas=None
    eventQueue=None

# Starts graphics mode
def SimpleGr(fg='yellow', bg='blue', bd='cyan', title = "SimplePython"):
    """ """
    global root
    global canvas
    global fg_color
    global scale
    global frame
    global images
    global image_on_canvas
    global eventQueue
    if root is not None:
        SimpleGrClose()

    fg_color=fg
    eventQueue=[]

    def keyPressed(event):
        eventQueue.append({ 'type':'key', 'char':event.char })

    def mouseButton(event):
        eventQueue.append({ 'type':'click', 'x':event.x//scale, 'y':event.y//scale })

    def onExit(event=None):
        SimpleGrClose()

    root = Tk()
    root.configure(bg=bd)
    root.title(title)

    scale=int(max(1,min(root.winfo_screenwidth()/(WIDTH*2), root.winfo_screenheight()/(HEIGHT*2))))

    root.geometry("%dx%d+%d+%d" % (WIDTH*1.1*scale, HEIGHT*1.1*scale, 0, 0))

    px_w = WIDTH*scale
    px_h = HEIGHT*scale

    canvas = Canvas( root, width=px_w, height=px_h, bg=bg, bd=0, highlightthickness=0, insertwidth=0, selectborderwidth=0, insertborderwidth=0 )
    canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    images= {}

    images[True] = PhotoImage(width=px_w, height=px_h)
    images[False] = PhotoImage(width=px_w, height=px_h)
    frame=True
    image_on_canvas=canvas.create_image((px_w/2, px_h/2), image=images[False], state="normal")

    canvas.bind("<Button-1>", mouseButton)
    root.bind("<Key>", keyPressed)
    root.bind('<Escape>', onExit)
    root.protocol("WM_DELETE_WINDOW", onExit)

    root.update()


# changes UI colors
def SimpleGrColor(fg=None, bg=None, bd=None):
    """ """
    global fg_color
    if root is None:
        return
    if is_color_like(fg):
        fg_color=fg
    if is_color_like(bg):
        canvas.configure(bg=bg)
    if is_color_like(bd):
        root.configure(bg=bd)

# Draws to current framebuffer
def SimpleGrPlot( x, y, x2 = None, y2 = None, color = None):
    """ """
    if x2 is None:
        x2, y2 = x+1, y+1
    x, y, x2, y2 = min(max(min(x, x2),0),WIDTH), min(max(min(y, y2),0),HEIGHT), min(max(max(x, x2),0),WIDTH), min(max(max(y, y2),0),HEIGHT)
    if color is None:
        color=fg_color
    if root is not None and is_color_like(color):
        images[frame].put(color, (int(x*scale),int(y*scale),int(x2*scale),int(y2*scale)))

# Displays current framebuffer and starts with a copy of the framebuffer
def SimpleGrFlipFrameCopy():
    """ """
    global frame
    if root is None:
        return
    canvas.itemconfig(image_on_canvas, image = images[frame])
    root.update()
    if root is None:
        return
    frame=not frame
    images[frame]=images[not frame].copy()

# Displays current framebuffer and starts with a blank framebuffer
def SimpleGrFlipFrameBlank():
    """ """
    global frame
    if root is None:
        return
    canvas.itemconfig(image_on_canvas, image = images[frame])
    root.update()
    if root is None:
        return
    frame=not frame
    images[frame].blank()

# Hands Control off program to UI events
def SimpleGrExit():
    """ """
    if root is not None:
        root.mainloop()
    exit(0)

# returns next UI input event, or Exit event if UI closed or None if not
def SimpleGrPollEvent():
    """ """
    if root is None:
        return { 'type':'exit' }
    else:
        root.update()
        if eventQueue is not None and len(eventQueue) > 0:
            return eventQueue.pop(0)
    return None


# Main Program unit tests for library
if __name__ == "__main__":
    from time import sleep

    # Test Screen Clear
    SimpleClear()


    # Create 1, 2 and 3 dimensional lists
    a = SimpleDim( 5 )
    print(a)
    a = SimpleDim( 5, 4 )
    print(a)
    a = SimpleDim( 5, 4, 3 )
    print(a)

    print (is_color_like('Saddlebrown'))
    print (is_color_like('#F0123A'))
    print (is_color_like('red'))
    print (is_color_like('marzian'))
    print (get_named_colors_mapping())
    print (is_color_like(None))

    SimpleGrColor('Saddlebrown')

    SimpleBeep()

    # Test Graphics mode
    SimpleGr()

    #help(Canvas)
    #print( canvas.config())
    #exit(0)

    SimpleGrPlot( 0, 0 )
    SimpleGrPlot( 0, 1 )
    SimpleGrPlot( 1, 0 )
    SimpleGrPlot( 1, 1 )

    SimpleGrPlot( 20, 20, 0, 0, 'green' )

    SimpleGrPlot( 50, 20, 30, -1 )

    for x in range(WIDTH):
        #y = int(HEIGHT/2 + HEIGHT/4 * sin(x/30.0))
        y = int(HEIGHT/2 + HEIGHT/4 * (2.71828**((x/30.0)*complex(0,1))).real)
        SimpleGrPlot( x, y )

    SimpleGrFlipFrameCopy()
    SimpleGrColor('Saddlebrown')
    SimpleGrPlot( 2, 2,  100, 100)
    sleep(2)
    print( 1 )
    SimpleGrFlipFrameBlank()
    SimpleGrColor('#FF0000','black','white')
    for x in range(WIDTH):
        #y = int(HEIGHT/2 + HEIGHT/4 * sin(x/30.0))
        y = int(HEIGHT/2 + HEIGHT/4 * (2.71828**((x/30.0)*complex(0,1))).real)
        SimpleGrPlot( x, y )

    sleep(2)
    print( 2 )
    SimpleGrColor('yellow')
    SimpleGrFlipFrameCopy()
    SimpleGrPlot( 2, 2,  100, 100)
    SimpleGrColor('tan')
    SimpleGrPlot( 150, 150, 50, 50)
    sleep(2)
    print( 3 )
    SimpleGrFlipFrameBlank()
    sleep(2)
    print( 4 )

    print(root.winfo_rgb('Saddlebrown'))
    print(root.winfo_rgb('#FFFF00'))


    print("USE WASD or mouse to move around, Q to quit.")
    x=WIDTH/2
    y=HEIGHT/2
    run=True
    while run:
        ev = SimpleGrPollEvent()
        if ev is not None:
            print(ev)
            if ev['type'] == 'exit':
                run = False
            elif ev['type'] == 'key':
                if ev['char'] == 'q' :
                    run = False
                elif ev['char'] == 'w' :
                    y=y-1
                    SimpleGrPlot( x, y,  x-10, y-10)
                    SimpleGrFlipFrameBlank()
                elif ev['char'] == 'a' :
                    x=x-1
                    SimpleGrPlot( x, y,  x-10, y-10)
                    SimpleGrFlipFrameBlank()
                elif ev['char'] == 's' :
                    y=y+1
                    SimpleGrPlot( x, y,  x-10, y-10)
                    SimpleGrFlipFrameBlank()
                elif ev['char'] == 'd' :
                    x=x+1
                    SimpleGrPlot( x, y,  x-10, y-10)
                    SimpleGrFlipFrameBlank()
            elif ev['type'] == 'click':
                    x=ev['x']
                    y=ev['y']
                    SimpleGrPlot( x, y,  x-10, y-10)
                    SimpleBeep()
                    SimpleGrFlipFrameBlank()


    SimpleGrFlipFrameBlank()
    SimpleGrPlot(0,0,WIDTH,HEIGHT)
    SimpleGrFlipFrameBlank()
    SimpleGrExit()


