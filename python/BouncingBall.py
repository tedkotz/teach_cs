#!/usr/bin/env python

from SimplePython import *
from time import sleep

__author__ = "<My Name>"

SimpleGr( 'magenta', 'black', 'green' )
x=WIDTH/2
y=HEIGHT/2
BALL_SIZE = 5
vx=3
vy=1.5
running = True

while( running ):
    # Draw Current Frame
    SimpleGrPlot( x, y, x+BALL_SIZE, y+BALL_SIZE )
    SimpleGrFlipFrameBlank()

    # Calculate Next frame postions
    x, y = x + vx, y + vy
    if x <= 0:
        vx = abs(vx)
        SimpleBeep()
    elif x > WIDTH - BALL_SIZE:
        vx = -abs(vx)
        SimpleBeep()
    if y <= 0:
        vy=abs(vy)
        SimpleBeep()
    elif y > HEIGHT - BALL_SIZE:
        vy=-abs(vy)
        SimpleBeep()

    # Limit Framerate and CPU usage
    sleep(0.015)

    # check for user input
    ev = SimpleGrPollEvent()
    if ev is not None and ev['type'] == 'exit':
        running = False

SimpleGrExit()
