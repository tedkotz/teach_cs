#!/usr/bin/env python3
""" A graphical toy that animates a little block that bounces off the wall, while falling to the floor and slowing down due to drag"""

__author__ = "<My Name>"

from SimplePython import *
from time import sleep


DRAG = 0.99
GRAV = 0.5

def AnimateBall( ball ):
    """ Draws the block described by ball to the current SimpleGr frame and calculates its next position and handles wall collisions, gravity and drag."""
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
        vx = abs(vx)
        collision = True
    elif x > WIDTH - size:
        vx = -abs(vx)
        collision = True
    if y <= 0:
        vy=abs(vy)
        collision = True
    elif y > HEIGHT - size:
        vy=-abs(vy)
        # Check if collision was fast enough to matter
        if vy < -1:
            collision = True
    else:
        # Apply gravity as constant downward velocity change
        vy=vy+GRAV

    # Apply drag as constant fraction of speed
    ball['vx']=DRAG*vx
    ball['vy']=DRAG*vy
    ball['x']=x
    ball['y']=y
    return collision




def ModularPhysicsBounce():
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
    ModularPhysicsBounce()
