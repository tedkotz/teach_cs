#!/usr/bin/env python3
""" A graphical toy that animates a little block that bounces off the wall making a little sound with each collision """

__author__ = "<My Name>"

from SimplePython import *
from time import sleep



def AnimateBall( ball ):
    """ Draws the block described by ball to the current SimpleGr frame and calculates its next position and handles wall collsions."""
    x=ball['x']
    y=ball['y']
    vx=ball['vx']
    vy=ball['vy']
    size=ball['size']
    collision = False

    # Draw Current Frame
    SimpleGrPlot( x, y, x+size, y+size, color=ball['color'] )

    # Calculate Next frame postions
    x, y = x + vx, y + vy

    # Check for collision with walls.
    if x <= 0:
        ball['vx'] = abs(vx)
        collision = True
    elif x > WIDTH - size:
        ball['vx'] = -abs(vx)
        collision = True
    if y <= 0:
        ball['vy']=abs(vy)
        collision = True
    elif y > HEIGHT - size:
        ball['vy']=-abs(vy)
        collision = True

    ball['x']=x
    ball['y']=y
    return collision




def ModularBounce():
    """ This function opens a graphics context and animates a bouncing ball until it is closed """
    SimpleGr( 'magenta', 'black', 'green' )
    BALL_SIZE = 5
    myBall = {
        'x':WIDTH/2,
        'y':HEIGHT/2,
        'vx':3,
        'vy':1.5,
        'size':BALL_SIZE,
        'color':'red'}
    running = True

    while( running ):
        # Draw Current Frame
        if AnimateBall(myBall):
            SimpleBeep()
        SimpleGrFlipFrameBlank()

        # Limit Framerate and CPU usage
        sleep(0.015)

        # check for user input
        ev = SimpleGrPollEvent()
        if ev is not None and ev['type'] == 'exit':
            running = False

    SimpleGrExit()

if __name__ == "__main__":
    ModularBounce()
