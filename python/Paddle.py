#!/usr/bin/env python3
""" A graphical toy that animates a little block that bounces off the wall making a little sound with each collision """

__author__ = "<My Name>"

from SimplePython import *
from ModularBounce import AnimateBall
from time import sleep



def AnimatePaddle( paddle ):
    """ Draws the block described by paddle."""
    x=paddle['x']
    y=paddle['y']
    xsize=paddle['xsize']
    ysize=paddle['ysize']
    collision = False

    # Check for collision with walls.
    if x < 0:
        x=0
        ball['x'] = x
        collision = True
    elif x > WIDTH - xsize:
        x = WIDTH - xsize
        ball['x'] = x
        collision = True
    if y < 0:
        y=0
        ball['y']=0
        collision = True
    elif y > HEIGHT - ysize:
        y=HEIGHT - ysize
        ball['y']=y
        collision = True

    # Draw Current Frame
    SimpleGrPlot( x, y, x+xsize, y+ysize, color=paddle['color'] )

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
    myPaddle = {
        'x':20,
        'y':HEIGHT/2,
        'xsize':5,
        'ysize':24,
        'color':'yellow'}
    running = True

    while( running ):
        # Draw Current Frame
        if AnimateBall(myBall):
            SimpleBeep()

        AnimatePaddle(myPaddle)
        SimpleGrFlipFrameBlank()

        # Limit Framerate and CPU usage
        sleep(0.015)

        # check for user input
        ev = SimpleGrPollEvent()
        if ev is not None:
            if ev['type'] == 'exit':
                running = False
            elif ev['type'] == 'key':
                if ev['char'] == 'q' :
                    myPaddle['y']=myPaddle['y']-3
                elif ev['char'] == 'a' :
                    myPaddle['y']=myPaddle['y']+3



    SimpleGrExit()

if __name__ == "__main__":
    ModularBounce()
