#!/usr/bin/env python3
""" A graphical toy that animates a bunch of little blocks that bounces off the wall making a little sound with each collision """

__author__ = "<My Name>"

from SimplePython import *
from ModularBounce import AnimateBall
#from ModularPhysicsBounce import AnimateBall
from time import sleep

def ApplyAttraction( ball, attractor, attraction ):
    """ Adjusts the velocities of ball based on the attraction to atractor """
    xdist = attractor['x'] - ball['x']
    ydist = attractor['y'] - ball['y']

    distSQR = max(1,(xdist*xdist + ydist*ydist))
    dist = distSQR**0.5
    ball['vx']= ball['vx'] + attraction*xdist/(ball['size']*distSQR*dist)
    ball['vy']= ball['vy'] + attraction*xdist/(ball['size']*distSQR*dist)




def MoreBalls():
    """ This function opens a graphics context and animates a bouncing ball until it is closed """
    SimpleGr( 'magenta', 'black', 'green' )
    BALL_SIZE = 5
    ballPit = [
        { 'x':180, 'y':200, 'vx':6,  'vy':-1,  'size':3, 'color':'red'},
        { 'x':100, 'y':180, 'vx':-4, 'vy':1,   'size':4, 'color':'cyan'},
        { 'x':280, 'y':90,  'vx':2,  'vy':-2,  'size':5, 'color':'yellow'},
        { 'x':230, 'y':60,  'vx':-1, 'vy':4,   'size':6, 'color':'magenta'},
        { 'x':140, 'y':120, 'vx':1,  'vy':-6,  'size':7, 'color':'violet'} ]
    running = True

    while( running ):
        # Draw Current Frame
        collision = False
        for ball in ballPit:
            if AnimateBall(ball):
                collision = True

        #if collision:
        #    SimpleBeep()
        SimpleGrFlipFrameBlank()

        for ball in ballPit:
            for ball2 in ballPit:
                if ball != ball2:
                    ApplyAttraction(ball, ball2, ball['size']*ball2['size']*2)

        # Limit Framerate and CPU usage
        sleep(0.015)

        # check for user input
        ev = SimpleGrPollEvent()
        if ev is not None and ev['type'] == 'exit':
            running = False

    SimpleGrExit()

if __name__ == "__main__":
    MoreBalls()
