__author__ = 'lenovo'
# coding=utf-8

import turtle
from fractions import gcd
import math
import random
from datetime import datetime
import Image


class Spiro:
    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False
        # set the parameters
        self.setparams(xc, yc, col, R, r, l)
        # initialize the drawing
        self.restart()

    # set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        # the Spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to its smallest form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r // gcdVal
        # get ratio of radii
        self.k = r / float(R)
        # set the color
        self.t.color(*col)
        # store the current angle
        self.a = 0

    # restart the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False
        # show the turtle
        self.t.showturtle()  # 展示海龟图表，防止被隐藏
        # go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        # 此处是套数学公式
        x, y = self.getXandY(a)
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x, y = self.getXandY(a)
            self.t.setpos(self.xc + x, self.yc + y)
            self.t.setheading()
        # drawing is now done so hide the turtle cursor
        self.t.hideturtle()

    # update  by one step
    def update(self):
        # skip the rest of the steps if done
        if self.drawingComplete:
            return
        # increment the angle
        self.a += self.step
        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x, y = self.getXandY(a)
        self.t.setpos(self.xc + x, self.yc + y)
        # if drawing is complete, set the flag
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()
    def clear(self):
        self.t.clear()


    def getXandY(self, a):
        R, k, l = self.R, self.k, self.l
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        return x, y


class SpiroAnimator:
    # constructor
    def __init__(self, N):
        # set the timer value in milliseconds
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # create the Spiro objects
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            # call timer
            turtle.ontimer(self.update, self.deltaT)

            # generate random parameters

    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)  # 随机生成下一个实数，它在 [x, y) 范围内。
        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)
        col = (random.random(), random.random(), random.random())
        return (xc, yc, col, R, r, l)

     # restart spiro drawing
    def restart(self):
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro.setparams(*rparams)
            # restart drawing
            spiro.restart()

    def update(self):
        # update all spiros
        nComplete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # restart if all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()
        # call the timer
        turtle.ontimer(self.update(),self.deltaT)

    # toggle turtle cursor on and off
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


def saveDrawing():
    # hide the turtle cursor
    turtle.hideturtle()
    # generate unique filenames
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-'+dateStr
    print("saving drawing to %s.eps/png" %fileName)
    # get the tkinter canvas
    canvas = turtle.getcanvas()
    # save the drawing as a postscript image
    canvas.postscript(file=fileName+'.eps')
    # use the Pillow module to convert the postscript image file to PNG
    img = Image.open(fileName+'.eps')
    # img = img.resize((100, 100), Image.ANTIALIAS)
    img.save(fileName+'.png')
    # show the turtle cursor
    turtle.showturtle()

import argparse
def main():
    descStr= "参数解析，生成海龟爬行图"
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--sparams',nargs=3,dest='sparams',required=False,help="The three arguments in sparams: R,r,l .")
    # parse args
    args = parser.parse_args()

    # set the width of the drawing widnow to 80 percent of the screen width
    turtle.setup(width=0.8)
    # set the cursor shape to turtle
    turtle.shape('turtle')
    # set the title to Spirographs!
    turtle.title('Spirographs!')
    # add the key handler to save our drawings
    turtle.onkey(saveDrawing,"s")# 按下s时调用 saveDrawing方法
    # start listening
    turtle.listen()

    # hide the main turtle cursor
    turtle.hideturtle()

    if args.sparams: # python spiro.py --sparams 300 100 0.9
        params = [float(x) for x in args.sparams]
        # draw the Spirograph with the given parameters
        col = (0.0,0.0,0.0)
        spiro = Spiro(0,0,col,*params)
        spiro.draw()
    else:
        # create the animator object
        spiroAnim = SpiroAnimator(4)
        # add a key handler to toggle the turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles,"t")
        # add a key handler to restart the animation
        turtle.onkey(spiroAnim.restart(),"space")

    # start the turtle main loop
    turtle.mainloop()

import ImageFilter
def own():
    img = Image.open("D:\随机数.png");
    img = img.filter(ImageFilter.BLUR)
    img.save("D:\随机数02.png");
# call main
if __name__ == "__main__":
    # main()
    own()


