#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:53:56 2019

@author: Asus
"""

# import logging as lg
from random import randrange


class ZGame():
    '''
    classdocs
    '''

    WALL = 'w'

    def __init__(self, log):
        '''
        Constructor
        '''

        # Init. logging
        self.__log = log

        self.__playground = []
        self.__playground_size = ()
        self.__hero = None
        self.__hero_direction = 'r'
        self.__path = []
        self.__asset_dct = {}

    @property
    def playground(self):
        """getter"""
        return self.__playground

    @property
    def playground_size(self):
        """getter"""
        return self.__playground_size

    @property
    def assets(self):
        """getter"""
        return self.__asset_dct

    def init_playground(self):
        '''
        Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""
        '''

        self.__playground_size = ()

        filename = "level.dat"
        n_row = 0

        try:
            with open(filename, "r") as file:
                self.__playground = []

                for line_idx, line in enumerate(file):

                    row = []

                    for sprite_idx, sprite in enumerate(line):

                        if sprite_idx == 0:
                            sprt_idx_0 = len(line.replace('\n', ''))

                        if sprite != '\n':
                            row.append(sprite)

                            if sprite == 'i':
                                self.__asset_dct['hero'] = {
                                    'pos_x': sprite_idx, 'pos_y': line_idx}
                                self.__log.debug(
                                    'Hero initial position [{}, {}]'.format(
                                        self.__asset_dct['hero']['pos_x'],
                                        self.__asset_dct['hero']['pos_y']))

                            if sprite == 'o':
                                self.__asset_dct['guard'] = {
                                    'pos_x': sprite_idx, 'pos_y': line_idx}
                                self.__log.debug(
                                    'Guard initial position [{}, {}]'.format(
                                        sprite_idx, line_idx)
                                    )

                            if sprite == 'p':
                                self.__path.append((sprite_idx, line_idx))

                    self.__playground.append(row)
                    n_row = line_idx+1

        except FileNotFoundError as err:
            self.__log.critical("\n# <Exception> {} \n".format(err))

        self.__log.debug("N row(s): {}".format(n_row))
        n_column = sprt_idx_0
        self.__log.debug("N column(s): {}".format(n_column))

        self.__playground_size = (n_column, n_row)

        # Place assets
        path_len = len(self.__path)
        asset_lst = ['n', 't', 'e']

        for asset in asset_lst:

            pos_idx = randrange(path_len)

            pos_x = self.__path[pos_idx][0]
            pos_y = self.__path[pos_idx][1]

            self.__asset_dct[asset] = {'pos_x': pos_x, 'pos_y': pos_y}
            self.__playground[pos_y][pos_x] = asset

            del self.__path[pos_idx]
            path_len = path_len - 1

    def move_hero(self, direction):
        '''
        docstring
        '''

        message = ('', 0)

        hero_pos_x = self.__asset_dct['hero']['pos_x']
        hero_pos_y = self.__asset_dct['hero']['pos_y']

        if direction == 'up':
            if hero_pos_y > 0:
                self.__log.debug('Expected playground {}'.format(
                    self.__playground[hero_pos_y-1][hero_pos_x]))
                if self.__playground[hero_pos_y-1][hero_pos_x] != self.WALL:
                    hero_pos_y = hero_pos_y - 1

        if direction == 'right':
            if hero_pos_x < self.__playground_size[0] - 1:
                self.__log.debug('Expected playground {}'.format(
                    self.__playground[hero_pos_y][hero_pos_x+1]))
                if self.__playground[hero_pos_y][hero_pos_x+1] != self.WALL:
                    hero_pos_x = hero_pos_x + 1

        if direction == 'down':
            if hero_pos_y < self.__playground_size[1] - 1:
                self.__log.debug('Expected playground {}'.format(
                    self.__playground[hero_pos_y+1][hero_pos_x]))
                if self.__playground[hero_pos_y+1][hero_pos_x] != self.WALL:
                    hero_pos_y = hero_pos_y + 1

        if direction == 'left':
            if hero_pos_x > 0:
                self.__log.debug('Expected playground {}'.format(
                    self.__playground[hero_pos_y][hero_pos_x-1]))
                if self.__playground[hero_pos_y][hero_pos_x-1] != self.WALL:
                    hero_pos_x = hero_pos_x - 1

        self.__hero_direction = direction
        self.__log.debug('Hero position [{}, {}] on playground {}'.format(
            hero_pos_x, hero_pos_y,
            self.__playground[hero_pos_y][hero_pos_x]))

        self.__asset_dct['hero']['pos_x'] = hero_pos_x
        self.__asset_dct['hero']['pos_y'] = hero_pos_y

        asset_type = self.__playground[hero_pos_y][hero_pos_x]
        if asset_type in ['n', 't', 'e']:
            del self.__asset_dct[asset_type]
            self.__playground[hero_pos_y][hero_pos_x] = 'p'
            self.__log.debug('{}'.format(self.__asset_dct))
            message = ('object', asset_type)

            if not any(k in ['n', 't', 'e'] for k in self.__asset_dct):
                message = ('object', 's')

        if self.__playground[hero_pos_y][hero_pos_x] == 'o':
            if any(k in ['n', 't', 'e'] for k in self.__asset_dct):
                message = ('end', False)
            else:
                message = ('end', True)

        return message      # , (hero_pos_x, hero_pos_y), direction


if __name__ == '__main__':

    import logging as lg

    lg.basicConfig(level=lg.DEBUG)
    lg.debug('Enable log')
    lg.info('Start Application')

    game = ZGame(lg)
    game.init_playground()
    game.move_hero('right')
    game.move_hero('down')
    game.move_hero('left')
    game.move_hero('up')
    game.move_hero('left')
    game.move_hero('up')
    game.move_hero('down')
    game.move_hero('right')
