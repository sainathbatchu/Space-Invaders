import pygame

#initialize
pygame.init()

#screen ((l)x-axis,(b)y-axis)
screen = pygame.display.set_mode((1000,600))

#title and icon-32px-png-@flaticon
pygame.display.set_caption(' Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
