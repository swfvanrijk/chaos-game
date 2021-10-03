# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:16:27 2019

@author: SWFvanRijk
"""

import matplotlib.pyplot as plt
import random as rdm
import math as m
import numpy as np

def RegularPolygonPoints(n,c):
    """
    Returns the coordinates of the vertices of a regular polygon with radius r 
    and n sides centered at coordinate c.
    """
    coord = []
    for i in range(n):
        x = m.cos(2*m.pi*i/n)+c[0]
        y = m.sin(2*m.pi*i/n)+c[1]
        coord.append([x,y])
    return(coord) 


def MovePoint(pos,points,s=0.5, k = 1000):
    """
    Moves the point a distance of s from the current position to a random vertex of the
    regular polygon and then does it again. k amounts of steps
    
    @params pos initial position,
    @return all the points the marker has been.
    """   
    
    x = [pos[0]] 
    y = [pos[1]]
    rdm.seed(1)    # comment out if you want randomness
    for i in range(k):
        n = len(points)
        r = int(rdm.random()*n)
        
        x.append(x[i] + (points[r][0] - x[i]) * s)
        y.append(y[i] + (points[r][1] - y[i]) * s)

        
    return(x,y)

vorm = RegularPolygonPoints(3,[0,0])


data = MovePoint([0,0.6],vorm,0.5)
    
   
t = np.arange(len(data[0]))

plt.scatter(data[1], data[0], c=t)
plt.title("initial conditions [0, 0.6]")
plt.show()
#plt.xlim(-70,70)
#plt.ylim(-70,70)
#plt.savefig("chaos.pdf")


### analytic solutions?

#        phi=(1+m.sqrt(5))/2
#        pX = pX + (points[r][0]-pX)*(n-2)/(n-1)
#        pY = pY + (points[r][1]-pY)*(n-2)/(n-1)

