# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:42 2019

@author: mtt
"""

# import sys
# import os
import argparse
import logging as lg

import pygame.mixer
from pygame import locals as pg_const


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

    main_win = pygame.display.set_mode((640, 480))       # , pg_const.RESIZABLE

#    fond = pygame.image.load("background.jpg").convert()
#    main_win.blit(fond, (0,0))


    wall_surf = pygame.image.load("structures.png").convert_alpha()
    wall_surf = pygame.transform.scale(wall_surf, (832,256))
#    wall_pos = wall_surf.get_rect()
#    main_win.blit(wall_surf, wall_pos)

    # crop an element
    wall_top_left_surf = pygame.transform.chop(
            pygame.transform.chop(wall_surf, (64,64,wall_surf.get_width()-64,wall_surf.get_height()-64)),
            (0,0,32,32))
    print(wall_top_left_surf)
    wall_top_left_pos = wall_top_left_surf.get_rect()
    print(wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_surf.get_rect().move(50,50)
    main_win.blit(wall_top_left_surf, wall_top_left_pos)


    hero_surf = pygame.image.load("MacGyver.png").convert_alpha()
    hero_surf = pygame.transform.scale(hero_surf, (32,32))
    hero_pos = hero_surf.get_rect()
    hero_pos = hero_pos.move(120,120)
    print(hero_pos)
    main_win.blit(hero_surf, hero_pos)

    guard_surf = pygame.image.load("Gardien.png").convert_alpha()
    guard_surf = pygame.transform.scale(guard_surf, (32,32))
#    guard_pos = guard_surf.get_rect()
    guard_pos = guard_surf.get_rect().move(50,50)

    main_win.blit(guard_surf, guard_pos)

    pygame.display.flip()


    flag = False

    while(flag == False):

        for event in pygame.event.get():

            if event.type == pg_const.QUIT:
                flag = True

            if event.type == pg_const.KEYDOWN:

                if event.key == pg_const.K_DOWN:
                    hero_pos = hero_pos.move(0,3)

                if event.key == pg_const.K_UP:
                    hero_pos = hero_pos.move(0,-3)

                if event.key == pg_const.K_LEFT:
                    hero_pos = hero_pos.move(-3,0)

                if event.key == pg_const.K_RIGHT:
                    hero_pos = hero_pos.move(3,0)


#        main_win.blit(fond, (0,0))
#        main_win.blit(wall_surf, wall_pos)
        main_win.blit(wall_top_left_surf, wall_top_left_pos)

#        print(hero_pos)
        main_win.blit(hero_surf, hero_pos)
        main_win.blit(guard_surf, guard_pos)

        pygame.display.flip()




