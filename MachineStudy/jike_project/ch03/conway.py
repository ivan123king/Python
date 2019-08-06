__author__ = 'lenovo'
#coding=utf-8

import sys,argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON,OFF]

def randomGrid(N):
    """
    returns a grid of NxN random values
    :param N:
    :return:
    """
    # 从数组vals中随机生成 N*N个数据，其中0.2,0.8分别表示ON和OFF出现的概率，reshape(N,N)是把这N*N个数据重新变为N行N列的数组
    return np.random.choice(vals,N*N,p=[0.2,0.8]).reshape(N,N)

def addGlider(i,j,grid):
    """
    adds a glider with top-left cell at(i,j)
    :param i:
    :param j:
    :param grid:
    :return:
    """
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]]) # np.array的作用就是得到这个数组，没有任何改变
    grid[i:i+3,j:j+3] = glider

def update(frameNum,img,grid,N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum using toroidal boundary conditions
            # x and y wrap around so that the simulation
            # takes place on a toroidal surface
            total = int((grid[i,(j-1)%N]+grid[i,(j+1)%N]+
                         grid[(i-1)%N,j]+grid[(i+1)%N,j]+
                         grid[(i-1)%N,(j-1)%N]+grid[(i-1)%N,(j+1)%N]+
                         grid[(i+1)%N,(j-1)%N]+grid[(i+1)%N,(j+1)%N])/255)
            # apply Conway's rules
            if grid[i,j]==ON:
                if(total<2) or (total>3):
                    newGrid[i,j] = OFF
            else:
                if total==3:
                    newGrid[i,j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img
# main function
def main():
    # command line arguments are in sys.argv[1],sys.argv[2],....
    # sys.argv[0] is the script name and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Run Conway's Game of Life simulation.")
    # add arguments
    parser.add_argument('--grid-size',dest='N',required=False)
    parser.add_argument('--move-file',dest='movfile',required=False)
    parser.add_argument('--interval',dest='interval',required=False)
    parser.add_argument('--glider',action='store_true',required=False)
    parser.add_argument('--gosper',action='store_true',required=False)
    args = parser.parse_args()
    # set grid size
    N = 100 #细胞数
    if args.N and int(args.N)>8:
        N = int(args.N)
    # set animation update interval
    updateInterval = 50 #动画时间间隔
    if args.interval:
        updateInterval = int(args.interval)
    # declare grid
    grid = np.array([])
    # check if 'glider demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N,N)
        addGlider(1,1,grid)
    else:
        # populate grid with random on/off more off than on
        grid = randomGrid(N)
    # print(grid)
    #set up the animation
    fig,ax = plt.subplots()
    img = ax.imshow(grid,interpolation='nearest')
    ani = animation.FuncAnimation(fig,update,fargs=(img,grid,N),frames=10,interval=updateInterval,save_count=50)
    # number of frames?
    # set the output file
    if args.movfile:
        ani.save(args.movfile,fps=30,extra_args=['-vcodec','libx264'])
    plt.show()
# call main
if __name__=="__main__":
    main()

