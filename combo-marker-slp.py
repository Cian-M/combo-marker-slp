from slippi import Game
from slippi import event
import os
import sys

def main():
    if(len(sys.argv) > 1):
        rootDir = sys.argv[1]
    else:
        rootDir = "."
    for root, dirs, files in os.walk(rootDir):
        for f in files:
            if(f[len(f) - 4:] == ".slp"):
                mark(root, f)

def mark(root, f):
    game = Game(root + "/" + f)
    frames = game.frames
    found = [False, False, False, False]
    endSearch = [0, 0, 0, 0]
    markedFrames = []
    finishedFrames = []
    for i in range(len(frames)):
        frame = frames[i]
        ports = frame.ports
        for j in range(len(ports)):
            if(endSearch[j] < i):
                found[j] = False
            if(not ports[j]):
                continue
            if(ports[j].leader.pre.buttons.physical == event.Buttons.Physical.DPAD_DOWN):
                if(found[j]):
                    continue
                if(i < endSearch[j]):
                    markedFrames.append(i)
                    found[j] = True
                    continue;
                endSearch[j] = i + 120
    for frame in markedFrames:
        minute = 7 - (int(frame / 60 / 60))
        second = 62 - (int(frame / 60 % 60))
        frame = str(minute) + "-" + str(second)
        finishedFrames.append(frame)
    name = ""
    for frame in finishedFrames:
        name = name + str(frame) + ", "
    os.rename(r'' + root + "/" + f, r'' + root + "/" + name[:len(name) - 2] + '.slp')

        
main()
