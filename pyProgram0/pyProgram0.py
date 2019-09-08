#2019-9-8 23:12:21
#version 1.0.0

import interface.dll as dll
import pygame, sys
from pygame.locals import *

def refreash():
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            dll.pyEnd()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        dll.pyEnd()
   
def drawRect(screen, node, UnitSize):
    (x, y), color = node
    pygame.draw.rect(screen, color, (x, y, x+UnitSize, y+UnitSize), 0)
    pass

if __name__ == "__main__":
    args = dll.pyInit()
    (XBoundary, Boundary), UnitSize = args

    pygame.init()
    screen = pygame.display.set_mode((XBoundary*UnitSize, Boundary*UnitSize))
    pygame.display.set_caption("pyProgram")
    screen.fill((0,0,0))


    while True:

        dll.pyStep()

        nodes = dll.pyPassThrough()
        for node in nodes:
            drawRect(screen, node, UnitSize)
            pass
    
        #                                                                                   //Haor: update don't clean the screen
        refreash()


