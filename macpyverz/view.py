#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:42:35 2019

@author: mtt
"""


import pygame
from pygame import locals as pg_const

from model import ZGame


ASSET_SIZE = 32


class ZView():
    '''
    classdocs
    '''

    main_win = pygame.display.set_mode((480, 480 + ASSET_SIZE))
    # , pg_const.RESIZABLE
    playground_surf = pygame.image.load("background.jpg").convert()
    hero_surf = pygame.image.load("MacGyver.png").convert_alpha()
    guard_surf = pygame.image.load("Gardien.png").convert_alpha()
    needle_surf = pygame.image.load("aiguille.png").convert_alpha()
    ether_surf = pygame.image.load("ether.png")
    ether_surf.set_colorkey((1, 1, 1))
    syringe_surf = pygame.image.load("seringue.png").convert_alpha()
    tube_surf = pygame.image.load("tube_plastique.png")
    tube_surf.set_colorkey((255, 255, 255))

    def __init__(self, log):
        '''
        Constructor
        '''

        # Init. logging
        self.__log = log

        # Init. model
        self.game_mdl = ZGame(self.__log)
        self.game_mdl.init_playground()

        # Init. GUI
        pygame.init()

        # Init. main view

        # Init. playground surface
        wall_surf = pygame.image.load("structures.png").convert()
        wall_surf = pygame.transform.scale(wall_surf, (832, 256))

        # - Crop an element
        wall_top_left_surf = pygame.transform.chop(
            pygame.transform.chop(wall_surf,
                                  (64, 64,
                                   wall_surf.get_width()-64,
                                   wall_surf.get_height()-64)),
            (0, 0, 32, 32))
        self.__log.debug('{}'.format(wall_top_left_surf))
        wall_top_left_pos = wall_top_left_surf.get_rect()
        self.__log.debug('{}'.format(wall_top_left_pos))

        for row_idx, row in enumerate(self.game_mdl.playground):

            for sprite_idx, sprite in enumerate(row):

                if sprite == 'w':
                    self.playground_surf.blit(wall_top_left_surf,
                                              (sprite_idx*ASSET_SIZE,
                                               row_idx*ASSET_SIZE)
                                              )

        # Init. hero surface
        self.hero_surf = pygame.transform.scale(self.hero_surf,
                                                (ASSET_SIZE, ASSET_SIZE))

        # Init. guard surface
        self.guard_surf = pygame.transform.scale(self.guard_surf,
                                                 (ASSET_SIZE, ASSET_SIZE))

        # Init. needle surface
        self.needle_surf = pygame.transform.scale(self.needle_surf,
                                                  (ASSET_SIZE, ASSET_SIZE))

        # Init. ether surface
        self.ether_surf = pygame.transform.scale(self.ether_surf,
                                                 (ASSET_SIZE, ASSET_SIZE))

        # Init. syringe surface
        self.syringe_surf = pygame.transform.scale(self.syringe_surf,
                                                   (ASSET_SIZE, ASSET_SIZE))

        # Init. tube surface
        self.tube_surf = pygame.transform.scale(self.tube_surf,
                                                (ASSET_SIZE, ASSET_SIZE))

    def refresh_playground(self):
        '''
        docstring
        '''

        self.main_win.blit(self.playground_surf,
                           self.playground_surf.get_rect())

        for type_key, asset in self.game_mdl.assets.items():

            if type_key == 'hero':
                surf = self.hero_surf

            if type_key == 'guard':
                surf = self.guard_surf

            if type_key == 'n':
                surf = self.needle_surf

            if type_key == 't':
                surf = self.tube_surf

            if type_key == 'e':
                surf = self.ether_surf

            pos_x = asset['pos_x'] * ASSET_SIZE
            pos_y = asset['pos_y'] * ASSET_SIZE

            self.main_win.blit(surf, (pos_x, pos_y))

        pygame.display.flip()

    def run(self):
        '''
        docstring
        '''

        flag = False
        msg = ('', 0)
        pygame.key.set_repeat(400, 30)

        while flag is False:

            for event in pygame.event.get():

                if event.type == pg_const.QUIT:
                    flag = True

                if event.type == pg_const.KEYDOWN:

                    if event.key == pg_const.K_DOWN:
                        msg = self.game_mdl.move_hero('down')
    #                    hero_pos = hero_pos.move(0,3)

                    if event.key == pg_const.K_UP:
                        msg = self.game_mdl.move_hero('up')
    #                    hero_pos = hero_pos.move(0,-3)

                    if event.key == pg_const.K_LEFT:
                        msg = self.game_mdl.move_hero('left')
    #                    hero_pos = hero_pos.move(-3,0)

                    if event.key == pg_const.K_RIGHT:
                        msg = self.game_mdl.move_hero('right')
    #                    hero_pos = hero_pos.move(3,0)

                    if msg[0] == 'object':

                        print('object msg')
                        if msg[1] == 'n':
                            self.main_win.blit(self.needle_surf, (0, 480))
                            print('needle msg')

                        if msg[1] == 't':
                            self.main_win.blit(self.tube_surf, (1*ASSET_SIZE,
                                                                480))
                            print('tube msg')

                        if msg[1] == 'e':
                            self.main_win.blit(self.ether_surf, (2*ASSET_SIZE,
                                                                 480))
                            print('ether msg')

                        if msg[1] == 's':
                            self.main_win.blit(self.needle_surf, (0, 480))
                            self.main_win.blit(self.tube_surf,
                                               (1*ASSET_SIZE, 480))
                            self.main_win.blit(self.ether_surf,
                                               (2*ASSET_SIZE, 480))
                            self.main_win.blit(self.syringe_surf,
                                               (4*ASSET_SIZE, 480))

                            print('seringe msg')

                    if msg[0] == 'end':
                        flag = True

                        if msg[1] is True:
                            print('\\o/ You Win \\o/')
                        else:
                            print('X_X You Lose X_X')

                    self.refresh_playground()


if __name__ == '__main__':

    import logging as lg

    lg.basicConfig(level=lg.DEBUG)
    lg.debug('Enable log')
    lg.info('Start Application')

    view = ZView(lg)
    view.refresh_playground()
    view.run()
