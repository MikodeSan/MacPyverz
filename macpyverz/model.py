# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:53:56 2019

@author: Asus
"""

class ZGame(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

        # Credit
        self.__playground = []
        self.__hero = None
        self.__guard = None
        self.__element = None


    @property
    def playground(self):
        return self.__playground

    def init_playground(self):

        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""

        filename = "level.dat"
        with open(filename, "r") as file:
            self.__playground = []

            for line in file:
                row = []

                for sprite in line:

                    if sprite != '\n':
                        row.append(sprite)

                self.__playground.append(row)

#                print(self.__playground)


if __name__ == '__main__':

    game = ZGame()
    game.init_playground()
