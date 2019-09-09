#2019-9-8 23:12:21
#version 1.0.0
from MyLibrary.Monitor.Logger import savelog
savelog()


import interface.dll as dll

import pygame, sys
from pygame.locals import *

def refreash():
    """
        update()

        if end, return False
    """
    pygame.display.update()
    running = True
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if running == False:
        sys.exit()
        dll.pyEnd()
    return running

   
def drawRect(screen, node, UnitSize):
    (x, y), color = node
    pygame.draw.rect(screen, color, (x, y, x+UnitSize, y+UnitSize), 0)
    pass

def display(XBoundary, Boundary, UnitSize):
    pygame.init()
    screen = pygame.display.set_mode((XBoundary*UnitSize, Boundary*UnitSize))
    pygame.display.set_caption("pyProgram")
    screen.fill((0,0,0))
    return screen


#__main__
if __name__ == "__main__":
    args = dll.pyInit()
    (XBoundary, Boundary), UnitSize = args

    screen = display(XBoundary, Boundary, UnitSize)

    running = True
    while running:

        dll.pyStep()

        nodes = dll.pyPassThrough()
        for node in nodes:
            drawRect(screen, node, UnitSize)
            pass
    
        running = refreash()
