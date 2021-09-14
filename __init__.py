import pygame
import sys
import random
import os
from pygame.locals import *

FPS=30
S_WIDTH=289
S_HEIGHT=511
SCREEN= pygame.display.set_mode((S_WIDTH,S_HEIGHT)) # for display screen
GROUNDY=S_HEIGHT*0.8
BIRD_IMG="imagespy/bird1.png"
'''print(type(BIRD_IMG))
#brd='/imagespy/bird1.png'
#print(type(brd))'''
GROUND_IMG="imagespy/base.png"
PIPE_IMG="imagespy/pipe.png"
BG_IMG="imagespy/bg.png"
GAME_SPRITES={}



def main_screen():
    bird_x = int(S_WIDTH /4)
    bird_y = int((S_HEIGHT - GAME_SPRITES['bird'].get_height()) / 2)

    base_y = int(S_HEIGHT * 0.87)
    base_x = 0

    time=0
    bird_height=GAME_SPRITES['bird'].get_height()
    bg_x = 0
    bg_y = int((S_HEIGHT - GAME_SPRITES['background'].get_height()) / 2)

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while(True):

        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if bird_y > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        bird_y = bird_y + min(playerVelY, GROUNDY - bird_y - bird_height)



        SCREEN.blit(GAME_SPRITES['background'], (bg_x, bg_y))
        SCREEN.blit(GAME_SPRITES['base'], (0, base_y))
        SCREEN.blit(GAME_SPRITES['bird'], (bird_x, bird_y))
        pygame.display.update()





def window_screen():
    brd_x=int(S_WIDTH/2)
    brd_y=int((S_HEIGHT-GAME_SPRITES['bird'].get_height())/2)

    base_y=int(S_HEIGHT*0.87)
    base_x=0

    bg_x=0
    bg_y=int((S_HEIGHT-GAME_SPRITES['background'].get_height())/2)



    while(True):
        SCREEN.blit(GAME_SPRITES['background'], (bg_x, bg_y))
        SCREEN.blit(GAME_SPRITES['base'], (0, base_y))
        SCREEN.blit(GAME_SPRITES['bird'], (brd_x, brd_y))
        pygame.display.update()

        for k in pygame.event.get():
            if  k.type==QUIT or (k.type==KEYDOWN and k.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif k.type==KEYDOWN and (k.key==K_SPACE or k.key==K_UP):
                print("game is about to start")
                return


if __name__=='__main__':
    pygame.init()
    FPS_CLOCK= pygame.time.Clock()
    GAME_SPRITES['base']=(pygame.image.load('imagespy/base.png'))
    GAME_SPRITES['bird'] = (pygame.image.load(BIRD_IMG))
    GAME_SPRITES['background'] = (pygame.image.load(BG_IMG))
    GAME_SPRITES['pipe']=(pygame.image.load(PIPE_IMG),pygame.transform.rotate(pygame.image.load(PIPE_IMG),180))

    while(True):
        window_screen()
        main_screen()
        print("prg ends")