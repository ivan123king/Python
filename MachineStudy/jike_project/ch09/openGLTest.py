__author__ = 'lenovo'
#coding=utf-8

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-0.5,0.0)
    glVertex3f(0.5,-0.5,0.0)
    glVertex3f(0.5,0.5,0.0)
    glVertex3f(-0.5,0.5,0.0)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(400,400)
    glutCreateWindow(b"oldgl")
    glutDisplayFunc(display)
    glutMainLoop()

# if __name__=="__main__":
#     main()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow(b"oldgl")
glutDisplayFunc(display)
glutMainLoop()
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl
# 报错：  Attempt to call an undefined function glutInit, check for bool(glutInit) before calling