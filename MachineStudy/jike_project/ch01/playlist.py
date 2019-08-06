#coding=utf-8
__author__ = 'lenovo'

import plistlib
import re,argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


def findDuplicates(fileName):
    """查找重复的唱片，计数加一"""
    print('Finding duplicate tracks in %s...' %fileName)
    #read in a playlist
    plist = plistlib.readPlist(fileName)
    #get the tracks from the Tracks ddictionary
    tracks = plist['Tracks']
    #create a track name dictionary
    trackNames = {}
    #iterate through the tracks
    for trackId,track in tracks.items():
        try:
            name = track['Name'];
            duration = track['Total Time']
            #look for existing entries
            if name in trackNames:
                # if a name and duration match,increment the couunt
                # round the track length to the nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration,count+1)
                else:
                    # add dictionary entry as tuple (duration,count)
                    trackNames[name] = (duration,1)
        except:
            pass
    # store duplicates as (name,count) tuples 元组
    dups = []
    for k,v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1],k))
    # save duplicates to a file
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to dup.txt " %len(dups))
    else:
        print("No duplicate tracks found!")
    f = open("dups.txt","w")
    for val in dups:
        f.write("[%d] %s\n" %(val[0],val[1]))
    f.close()

def findDuplicatesByDuration(fileName):
    """查找重复的唱片，计数加一  自己写的，通过音乐时长找相同的"""
    print('Finding duplicate tracks in %s...' %fileName)
    #read in a playlist
    plist = plistlib.readPlist(fileName)
    #get the tracks from the Tracks ddictionary
    tracks = plist['Tracks']
    #create a track name dictionary
    trackDuration = {}
    #iterate through the tracks
    for trackId,track in tracks.items():
        try:
            name = track['Name'];
            duration = track['Total Time']
            #look for existing entries
            if duration in trackDuration:
                # if a name and duration match,increment the couunt
                # round the track length to the nearest second
                count = trackDuration[name][1]
                trackDuration[duration] = (name,count+1)
            else:
                # add dictionary entry as tuple (duration,count)
                trackDuration[duration] = (name,1)
        except:
            pass
    # store duplicates as (name,count) tuples 元组
    dups = []
    for k,v in trackDuration.items():
        if v[1] > 1:
            dups.append((v[1],v[0],k))
    # save duplicates to a file
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to dup.txt " %len(dups))
    else:
        print("No duplicate tracks found!")
    f = open("dups.txt","w")
    for val in dups:
        f.write("[%d] %s [%d]\n" %(val[0],val[1],val[2]))
    f.close()

def findCommonTracks(fileNames):
    """
    找出公共的歌曲
    :param fileNames:
    :return:
    """
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set()
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId,track in tracks.items():
            try:
                #add the track name to a set
                trackNames.add(track['Name'])
            except:
                pass
    #add to list
    trackNameSets.append(trackNames)
    # get the set of common tracks
    commonTracks = set.intersection(*trackNameSets) #求 trackNameSets中保存的set对象的交集
    # write to file
    if len(commonTracks) > 0:
        f = open("common.txt","wb")
        for val in commonTracks:
            s = "歌曲名：%s\n" % val
            f.write((s.encode("UTF-8")))
        f.close()
        print("%d common tracks found. "
              "Track names written to common txt. " % len(commonTracks))
    else:
        print(" No common tracks.")


def plotStats(fileName):
    """
    收集评分和歌曲时长，用来绘图
    :param fileName:
    :return:
    """
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the playlist
    tracks = plist['Tracks']
    #create lists of song ratings and track durations
    ratings = []
    durations = []
    # iterate through the tracks
    for trackId,track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass
    # ensure that valid data was collected
    if ratings == [] or durations==[]:
        print("No valid Album Rating/Total Time data in %s." %fileName)
        return

    #绘图
    x = np.array(durations,np.int32)
    # convert to minutes  转化为分钟单位
    x = x/60000.0
    y = np.array(ratings,np.int32)
    pyplot.subplot(2,1,1)
    pyplot.plot(x,y,'o')
    pyplot.axis([0,1.05*np.max(x),-1,110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')
    # plot histogram
    pyplot.subplot(2,1,2)
    pyplot.hist(x,bins=20) #绘制长直方图
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')
    # show plot
    pyplot.show()

def main():
    # crate parser
    descStr = """
        This program analyzes playlist files (.xml) exported from iTunes.
        """
    parser = argparse.ArgumentParser(description=descStr)
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()
    # add expected arguments
    group.add_argument('--common',nargs="*",dest='plFiles',required=False)
    group.add_argument("--stats",dest="plFile",required=False)
    group.add_argument("--dup",dest="plFileD",required=False)

    #parse args
    args = parser.parse_args()
    if args.plFiles:
        #find common tracks
        findCommonTracks(args.plFiles)
    elif args.plFile:
        #plot stats
        plotStats(args.plFile)
    elif args.plFileD:
        # find duplicate tracks
        findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")

# main method
if __name__ == '__main__':
    main()


"""
在命令行运行：python playlist.py --common test-data/maya.xml test-data/rating.xml 得到此中的重复歌曲
运行： python playlist.py --stats test-data/rating.xml 绘制评分，时长图  Figure_1.png
"""