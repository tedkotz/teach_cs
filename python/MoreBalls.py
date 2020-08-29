#!/usr/bin/env python3
""" A graphical toy that animates a bunch of little blocks that bounces off the wall making a little sound with each collision """

__author__ = "<My Name>"

from SimplePython import *
#from ModularBounce import AnimateBall
from ModularPhysicsBounce import AnimateBall
from time import sleep

def MoreBalls():
    """ This function opens a graphics context and animates a bouncing ball until it is closed """
    SimpleGr( 'magenta', 'black', 'green' )
    BALL_SIZE = 5
    ballPit = [
        { 'x':WIDTH/2, 'y':HEIGHT/2, 'vx':6,  'vy':-1,  'size':3, 'color':'red'},
        { 'x':WIDTH/2, 'y':HEIGHT/2, 'vx':-4, 'vy':1,   'size':4, 'color':'cyan'},
        { 'x':WIDTH/2, 'y':HEIGHT/2, 'vx':2,  'vy':-2,  'size':5, 'color':'yellow'},
        { 'x':WIDTH/2, 'y':HEIGHT/2, 'vx':-1, 'vy':4,   'size':6, 'color':'magenta'},
        { 'x':WIDTH/2, 'y':HEIGHT/2, 'vx':1,  'vy':-6,  'size':7, 'color':'violet'} ]
    running = True

    while( running ):
        # Draw Current Frame
        collision = False
        for ball in ballPit:
            if AnimateBall(ball):
                collision = True

        if collision:
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
    MoreBalls()
