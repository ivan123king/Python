__author__ = 'lenovo'
#coding=utf-8

import sys,random,argparse
from PIL import Image,ImageDraw

# create spacing/depth example
def createSpacingDepthExample():
    tiles = [ Image.open('data/a.png'),Image.open('data/b.png'),Image.open('data/c.png')]
    img = Image.new("RGB",(600,400),(0,0,0))
    spacing = [10,20,40]
    for j,tile in enumerate(tiles):
        for i in range(8):
            img.paste(tile,(10+i*(100+j*10),10+j*100))
    img.save('sdepth.png')

# create an image filled with random circles
def createRandomTile(dims):
    # create image
    img = Image.new("RGB",dims)
    draw = ImageDraw.Draw(img) #画圆圈
    # set the radius of a random circle to 1% of width or height,whichever is smaller
    r = int(min(*dims)/100) # python中的*运算符能将dims元组中的宽高解包
    # number of circles
    n = 1000
    # draw random circles
    for i in range(n):
        # 减 r 是为了让绘制的圆圈在图像中，而不会出现一半在图像外的场景
        x,y = random.randint(0,dims[0]-r),random.randint(0,dims[1]-r)
        fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        draw.ellipse((x-r,y-r,x+r,y+r),fill)
    return img

# tile a graphics file to create an intermediate image of a set size
def createTiledImage(tile,dims):
    # create the new image
    img = Image.new("RGB",dims)
    W,H = dims
    w,h = tile.size
    # calculate the number of tiles needed
    cols = int(W/w)+1
    rows = int(H/h)+1
    # paste the tiles into the image
    for i in range(rows):
        for j in range(cols):
            img.paste(tile,(j*w,i*h))
    # output the image
    return img

# create a depth map for testing
def createDepthMap(dims):
    dmap = Image.new('L',dims)
    dmap.paste(10,(200,25,300,125))
    dmap.paste(30,(200,150,300,250))
    dmap.paste(20,(200,275,300,375))
    return dmap

# given a depth map image and an input image
# create a new image with pixels shifted according to depth
def createDepthShiftedImage(dmap,img):
    # size check
    assert dmap.size == img.size
    # create shifted image
    sImg = img.copy()
    # get pixel access
    pixD = dmap.load()
    pixS = sImg.load()
    # shift pixels output based on depth map
    cols,rows = sImg.size
    for j in range(rows):
        for i in range(cols):
            xshift = pixD[i,j]/10
            xpos = i-140+xshift
            if xpos > 0 and xpos <cols:
                pixS[i,j] = pixS[xpos,j]
    return sImg

# given a depth map (image) and an input image
# create a new image with pixels shifted according to depth
def createAutostereogram(dmap,tile):
    # convert the depth map to single channel if needed
    if dmap.mode is not 'L':
        dmap = dmap.convert('L')
    # if no image is specified for a tile,create a random circles tile
    if not tile:
        tile = createRandomTile((100,100))
    # create an image by tiling
    img = createTiledImage(tile,dmap.size)
    # create a shifted image using depth map values
    sImg = img.copy()
    # get access to image pixels by loading the image object first
    pixD = dmap.load()
    pixS = sImg.load()
    # shift pixels horizontally based on depth map
    cols,rows = sImg.size
    for j in range(rows):
        for i in range(cols):
            xshift = pixD[i,j]/10
            xpos = i-tile.size[0]+xshift
            if xpos > 0 and xpos<cols:
                pixS[i,j] = pixS[xpos,j]
    return sImg

# main function
def main():
    # use sys.argv if needed
    print("creating autostereogram...")
    # create parser
    parser = argparse.ArgumentParser(description="Autostereogram...")
    # add expected arugments
    parser.add_argument("--depth",dest="dmFile",required=True)
    parser.add_argument("--tile",dest="tileFile",required=False)
    parser.add_argument("--out",dest="outFile",required=False)
    # parse args
    args = parser.parse_args()
    # set the out file
    outFile = "as.png"
    if args.outFile:
        outFile = args.outFile
    # set tile
    tileFile = False
    if args.tileFile:
        tileFile = Image.open(args.tileFile)
    # open depth map
    dmImg = Image.open(args.dmFile)
    # create stereogram
    asImg = createAutostereogram(dmImg,tileFile)
    # write output
    asImg.save(outFile)

# call main
if __name__=="__main__":
    main()

# 运行命令： python autos.py --depth data/stool-depth.png
# 使用随机生成的平铺图像 生成三维立体图像  as.png就是三维立体图像，我完全看不出来哪里立体