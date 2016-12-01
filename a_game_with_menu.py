'''
title: A game with a menu
author: semiTheBug
date: 161129
'''
## Import stuff
import pygame
import math
import random
import sys

## Definitions
SW = 800
SH = 600

screen = pygame.display.set_mode((SW, SH))

## Functions
def menu():
    menu_list = ["Continue","Volume","Quit"]
    menu_color = (180,180,180)
    selected = 0
    myfont = pygame.font.SysFont("californianfb", 25)
    open = True
    for i in range(0,200):
        #Fill the background with white color
        screen.fill((255,255,255))
        pygame.draw.rect(screen, menu_color,(150, 100, i*(SW-300)/200, i*(SH-200)/200))
        #Flip the screen
        pygame.display.flip()
    while open == True:
        #Fill the background with white color
        screen.fill((255,255,255))
        pygame.draw.rect(screen, menu_color,(150, 100, SW-300, SH-200))
        pygame.draw.rect(screen, (0,0,0),(160, 110, SW-320, SH-220),1)
        for i in range(0, len(menu_list)):
            label = myfont.render(menu_list[i], 1, (0,0,0))
            screen.blit(label, (250, 150+100*i))
            if i == selected:
                pygame.draw.rect(screen,(255,50,50),(200,150+100*i,20,20))
        #Flip the screen
        pygame.display.flip()
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Escape will quit the program
                if event.key == pygame.K_ESCAPE:
                    open = False
                if event.key == pygame.K_DOWN:
                    if selected < len(menu_list)-1:
                        selected += 1
                if event.key == pygame.K_UP:
                    if selected > 0:
                        selected -= 1
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        open = False
                    if selected == 2:
                        pygame.quit()
                        sys.exit()
    for i in range(200,0,-1):
        #Fill the background with white color
        screen.fill((255,255,255))
        pygame.draw.rect(screen, menu_color,(150, 100, i*(SW-300)/200, i*(SH-200)/200))
        #Flip the screen
        pygame.display.flip()
    

## Start the game loop
pygame.init()
while __name__=="__main__":
    #Set the frame count to 60 per second
    pygame.time.Clock().tick(60)
    #Fill the background with white color
    screen.fill((255,255,255))
    #Draw a rectangle for the menu
    #pygame.draw.rect(screen, (150, 150, 150),(150, 100, SW-300, SH-200))
    #Flip the screen
    pygame.display.flip()
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Escape will quit the program
            if event.key == pygame.K_ESCAPE:
                    menu()
                #pygame.quit()
                #sys.exit()

