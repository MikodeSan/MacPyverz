# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:53:56 2019

@author: Asus
"""

class ZGame():
    '''
    classdocs
    '''

    WALL = 'w'

    def __init__(self):
        '''
        Constructor
        '''

        # Credit
        self.__playground = []
        self.__playground_size = ()
        self.__hero = None
        self.__hero_pos_x = 0
        self.__hero_pos_y = 0
        self.__hero_direction = 'r'
#        self.__guard = None
#        self.__element = None


    @property
    def playground(self):
        """getter"""
        return self.__playground

    @property
    def playground_size(self):
        """getter"""
        return self.__playground_size


    def init_playground(self):

        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""

        self.__playground_size = ()

        filename = "level.dat"
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
                        self.__hero_pos_x = sprite_idx
                        self.__hero_pos_y = line_idx
                        print('Hero initial position [{}, {}]'.format(self.__hero_pos_x, self.__hero_pos_y))

                self.__playground.append(row)


            n_row = line_idx+1
            print("N row(s)", n_row)
            n_column = sprt_idx_0
            print("N column(s)", n_column)




        self.__playground_size = (n_column, n_row)


    def move_hero(self, direction):

        message = ('', 0)

        hero_pos_x = self.__hero_pos_x
        hero_pos_y = self.__hero_pos_y

        if direction == 'up':
            if hero_pos_y > 0:
                print('Playground', self.__playground[hero_pos_y-1][hero_pos_x])
                if self.__playground[hero_pos_y-1][hero_pos_x] != 'w':
                    self.__hero_pos_y = hero_pos_y - 1

        if direction == 'right':
            if hero_pos_x < self.__playground_size[0] - 1:
                print('Playground', self.__playground[hero_pos_y][hero_pos_x+1])
                if self.__playground[hero_pos_y][hero_pos_x+1] != 'w':
                    self.__hero_pos_x = hero_pos_x + 1

        if direction == 'down':
            if hero_pos_y < self.__playground_size[1] - 1:
                print('Playground', self.__playground[hero_pos_y+1][hero_pos_x])
                if self.__playground[hero_pos_y+1][hero_pos_x] != 'w':
                    self.__hero_pos_y = hero_pos_y + 1

        if direction == 'left':
            if hero_pos_x > 0:
                print('Playground', self.__playground[hero_pos_y][hero_pos_x-1])
                if self.__playground[hero_pos_y][hero_pos_x-1] != 'w':
                    self.__hero_pos_x = hero_pos_x - 1


        self.__hero_direction = direction
        print('Hero position [{}, {}]'.format(self.__hero_pos_x, self.__hero_pos_y))


        return message, (self.__hero_pos_x, self.__hero_pos_y), direction


if __name__ == '__main__':

    game = ZGame()
    game.init_playground()
    game.move_hero('right')
    game.move_hero('down')
    game.move_hero('left')
    game.move_hero('up')
    game.move_hero('left')
    game.move_hero('up')
    game.move_hero('down')
    game.move_hero('right')
