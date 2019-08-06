__author__ = 'lenovo'
#coding=utf-8
import turtle
import math
import argparse
import sys

def draw(type):

    t = turtle.Turtle()

    if type=="circle":
                #draw the circle
        total = 0
        while total< 3:
            total += 1
            x = 20;y = 30;r=100
            t.up()
            t.shape("turtle")
            t.setpos(x+r,y)
            t.down()

            for i in range(0,365,5):
                a = math.radians(i)
                t.setpos(x+r*math.cos(a),y+r*math.sin(a))
                t.setheading(a)
            t.clear()
        sys.exit()
    elif type=="square":
        x = 20; y = 30; x2 = 40*3;y2=40*4
        t.up()
        t.setpos(x,y)
        t.down()
        t.setpos(x2,y)
        t.setpos(x2,y2)
        t.setpos(x,y2)
        t.setpos(x,y)



def main():
    desStr = "choose which pattern you want drawing."
    parser = argparse.ArgumentParser(description=desStr)
    parser.add_argument("--pattern",dest="pattern",required=True,help="input circle,or square choose drawing,eg --pattern circle")
    args = parser.parse_args()
    draw(args.pattern)
    turtle.mainloop()

import numpy as np
def owntest():
    grid = np.random.choice([0,1,2,3,4],4*4).reshape(4,4)
    print(grid)
    print(grid[1:1+3,1:1+3])

if __name__=="__main__":
    # main()
    owntest()
