#!/usr/bin/env python

import os
import thread
from time import sleep
from Tkinter import *
from matplotlib.colors import is_color_like

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

root=None
canvas=None
frame=None
images=None
fg_color=None
scale=None
WIDTH=360
HEIGHT=240
image_on_canvas=None

def SimpleGr(fg='yellow', bg='blue', bd='cyan'):
    global root
    global canvas
    global fg_color
    global scale
    global frame
    global images
    global image_on_canvas
    fg_color=fg

    def key(event):
        print "pressed", repr(event.char)

    def mouseButton(event):
        print "clicked at", event.x, event.y
        canvas.focus_set()

    root = Tk()
    root.configure(bg=bd)

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    scale=int(max(1,min(w/(360*2), h/(240*2))))

    w = 1.1 * scale * 360
    h = 1.1 * scale * 240

    root.geometry("%dx%d+%d+%d" % (396*scale, 264*scale, 0, 0))

    px_w = WIDTH*scale
    px_h = HEIGHT*scale

    canvas = Canvas( root, width=px_w, height=px_h, bg=bg, bd=0)
    canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    images= {}

    images[True] = PhotoImage(width=px_w, height=px_h)
    images[False] = PhotoImage(width=px_w, height=px_h)
    frame=True
    image_on_canvas=canvas.create_image((px_w/2, px_h/2), image=images[False], state="normal")

    canvas.bind("<Key>", key)
    canvas.bind("<Button-1>", mouseButton)

    root.update()


def SimpleGrColor(fg=None, bg=None, bd=None):
    global fg_color
    if is_color_like(fg):
        fg_color=fg
    if is_color_like(bg):
        canvas.configure(bg=bg)
    if is_color_like(bd):
        root.configure(bg=bd)

def SimpleGrPlot( x, y, x2 = None, y2 = None):
    if x2 is None:
        x2, y2 = x+1, y+1
    images[frame].put(fg_color, (x*scale,y*scale,x2*scale,y2*scale))

def SimpleGrFlipFrameCopy():
    global frame
    canvas.itemconfig(image_on_canvas, image = images[frame])
    root.update()
    frame=not frame
    images[frame]=images[not frame].copy()

def SimpleGrFlipFrameBlank():
    global frame
    canvas.itemconfig(image_on_canvas, image = images[frame])
    root.update()
    frame=not frame
    images[frame].blank()

def SimpleGrExit():
    root.mainloop()
    exit(0)

def SimpleBeep():
    sys.stdout.write('\a')


# Main Program unit tests for library
if __name__ == "__main__":

    # Test Screen Clear
    SimpleClear()



    # Create 1, 2 and 3 dimensional lists
    a = SimpleDim( 5 )
    print(a)
    a = SimpleDim( 5, 4 )
    print(a)
    a = SimpleDim( 5, 4, 3 )
    print(a)


    SimpleBeep()

    # Test Graphics mode
    SimpleGr()


    SimpleGrPlot( 0, 0 )
    SimpleGrPlot( 0, 1 )
    SimpleGrPlot( 1, 0 )
    SimpleGrPlot( 1, 1 )

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
    SimpleGrColor('magenta')
    SimpleGrPlot( 50, 50,  150, 150)
    sleep(2)
    print( 3 )
    SimpleGrFlipFrameBlank()
    sleep(2)
    print( 4 )

    print(root.winfo_rgb('Saddlebrown'))
    print(root.winfo_rgb('#FFFF00'))

    SimpleGrExit()


