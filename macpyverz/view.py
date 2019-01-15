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



    def __init__(self):
        '''
        Constructor
        '''

        # Init. model
        self.game_mdl = ZGame()
        self.game_mdl.init_playground()


        # Init. GUI
        pygame.init()

        pygame.key.set_repeat(400, 30)


        # Init. main view
        self.main_win = pygame.display.set_mode((480, 640))       # , pg_const.RESIZABLE


        # Init. playground surface
        self.playground_surf = pygame.image.load("background.jpg").convert()

        wall_surf = pygame.image.load("structures.png").convert()
        wall_surf = pygame.transform.scale(wall_surf, (832,256))

        # - Crop an element
        wall_top_left_surf = pygame.transform.chop(
                pygame.transform.chop(wall_surf, (64,64,wall_surf.get_width()-64,wall_surf.get_height()-64)),
                (0,0,32,32))
        print(wall_top_left_surf)
        wall_top_left_pos = wall_top_left_surf.get_rect()
        print(wall_top_left_pos)

        for row_idx, row in enumerate(self.game_mdl.playground):

            for sprite_idx, sprite in enumerate(row):

                if sprite == 'w':
                    self.playground_surf.blit(wall_top_left_surf, (sprite_idx*ASSET_SIZE,row_idx*ASSET_SIZE))

        # Init. hero surface
        self.hero_surf = pygame.image.load("MacGyver.png").convert_alpha()
        self.hero_surf = pygame.transform.scale(self.hero_surf, (ASSET_SIZE,ASSET_SIZE))

        # Init. guard surface
        self.guard_surf = pygame.image.load("Gardien.png").convert_alpha()
        self.guard_surf = pygame.transform.scale(self.guard_surf, (ASSET_SIZE,ASSET_SIZE))

        # Init. needle surface
        self.needle_surf = pygame.image.load("aiguille.png").convert_alpha()
        self.needle_surf = pygame.transform.scale(self.needle_surf, (ASSET_SIZE,ASSET_SIZE))

        # Init. ether surface
        self.ether_surf = pygame.image.load("ether.png").convert_alpha()
        self.ether_surf = pygame.transform.scale(self.ether_surf, (ASSET_SIZE,ASSET_SIZE))

        # Init. syringe surface
        self.syringe_surf = pygame.image.load("seringue.png").convert_alpha()
        self.syringe_surf = pygame.transform.scale(self.syringe_surf, (ASSET_SIZE,ASSET_SIZE))

        # Init. tube surface
        self.tube_surf = pygame.image.load("tube_plastique.png").convert_alpha()
        self.tube_surf = pygame.transform.scale(self.tube_surf, (ASSET_SIZE,ASSET_SIZE))


    def refresh_playground(self):

        self.main_win.blit(self.playground_surf, self.playground_surf.get_rect())

        for asset in self.game_mdl.asset_lst:

            print(asset)

            if asset['type'] == 'hero':
                surf = self.hero_surf
            if asset['type'] == 'guard':
                surf = self.guard_surf
            if asset['type'] == 'n':
                surf = self.needle_surf
            if asset['type'] == 't':
                surf = self.tube_surf
            if asset['type'] == 'e':
                surf = self.ether_surf

            pos_x = asset['pos_x'] * ASSET_SIZE
            pos_y = asset['pos_y'] * ASSET_SIZE

            self.main_win.blit(surf, (pos_x, pos_y))

        pygame.display.flip()



#        hero_pos = hero_surf.get_rect()
#        hero_pos = hero_pos.move(120,120)
#        print(hero_pos)
#
#        main_win.blit(hero_surf, hero_pos)
#
#        # guard
#        guard_pos = guard_surf.get_rect().move(50,50)
#
#        main_win.blit(guard_surf, guard_pos)
#
#
#        # needle
#        main_win.blit(guard_surf, guard_pos)
#
#
#        pygame.display.flip()





if __name__ == '__main__':

    view = ZView()
    view.refresh_playground()

    flag = False
    msg = ('', 0)

    while(flag == False):


        for event in pygame.event.get():

            if event.type == pg_const.QUIT:
                flag = True

            if event.type == pg_const.KEYDOWN:

                if event.key == pg_const.K_DOWN:
                    msg, hero_pos, b = view.game_mdl.move_hero('down')
#                    hero_pos = hero_pos.move(0,3)

                if event.key == pg_const.K_UP:
                    msg, hero_pos, b = view.game_mdl.move_hero('up')
#                    hero_pos = hero_pos.move(0,-3)

                if event.key == pg_const.K_LEFT:
                    msg, hero_pos, b = view.game_mdl.move_hero('left')
#                    hero_pos = hero_pos.move(-3,0)

                if event.key == pg_const.K_RIGHT:
                    msg, hero_pos, b = view.game_mdl.move_hero('right')
#                    hero_pos = hero_pos.move(3,0)


            view.refresh_playground()

#        print(hero_pos)


        if msg[0] == 'win':
            print('!!! You Win !!!')
            flag = True


