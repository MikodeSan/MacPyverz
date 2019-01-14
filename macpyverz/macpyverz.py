# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:42 2019

@author: mtt
"""

import sys
import os
import argparse
import logging as lg

import pygame.mixer
from pygame.locals import *


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CVS or XML?""")
    parser.add_argument("-d", "--datafile", help="""the path of file to analyse""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Make the application talk!""")

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_arguments()

#    print('datafile path:', args.datafile)
    print('args:', args)

#    if args.verbose:
#        lg.basicConfig(level=lg.DEBUG)
#    else:
    lg.basicConfig(level=lg.DEBUG)
    print('Enable log', lg.info)
    lg.info('Enable log')

#    if args.extension == 'xml':
#        print('xml analysis')
#    elif args.extension == 'csv':
#        print('csv analysis')
#    else:
#        print('unknown file extension')

    lg.info('Start Application')

    pygame.init()

    pygame.key.set_repeat(400, 30)

    fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0,0))

    prs = pygame.image.load("perso.png").convert_alpha()
    pos_perso = prs.get_rect()
    fenetre.blit(prs, pos_perso)

    pygame.display.flip()


    flag = False

    while(flag == False):

        for event in pygame.event.get():

            if event.type == QUIT:
                flag = True

            if event.type == KEYDOWN:

                if event.key == K_DOWN:
                    pos_perso = pos_perso.move(0,3)

                if event.key == K_UP:
                    pos_perso = pos_perso.move(0,-3)

                if event.key == K_LEFT:
                    pos_perso = pos_perso.move(-3,0)

                if event.key == K_RIGHT:
                    pos_perso = pos_perso.move(3,0)


        fenetre.blit(fond, (0,0))
        fenetre.blit(prs, pos_perso)

        pygame.display.flip()




