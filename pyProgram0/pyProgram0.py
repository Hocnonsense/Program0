#2019-9-8 23:12:21
#version 1.0.0


if __name__ == "__main__":

	pass

#                                                                                       //Haor: add sys
import random, math, pygame, sys
from pygame.locals import *

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Demo")
screen.fill((0,0,100))

pos_x = 300
pos_y = 250
radius = 200
angle = 360
ori_angle = 0

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
#                                                                                       //Haor: change () to []
color = [r,g,b]

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    #increment angle
    angle += 1
    #                                                                                   //Haor: return to the start number
    if angle >= 360:
        angle = 0
    #                                                                                   //Haor: change the rules of color changing time and dict
    if ori_angle == angle:
        color[random.randint(0,2)] = random.randint(0,255)
        ori_angle = random.randint(0,360)

    #calculate coordinates
    x = math.cos( math.radians(angle) ) * radius
    y = math.sin( math.radians(angle) ) * radius

    #draw one step around the circle
    #                                                                                   //Haor: or '.rect(screen, color, (int(pos_x + x), int(pos_y + y),3,3), 10)'
    pos = ( int(pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, pos, 10, 0)

    #                                                                                   //Haor: update don't clean the screen
    pygame.display.update()
    


