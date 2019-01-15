# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:42 2019

@author: mtt
"""

# import sys
# import os
# import datetime
import argparse
import logging as lg

import pygame.mixer
from pygame import locals as pg_const

from model import ZGame


#def load_db(filename):
#
#    db = {}
#
##    print("\n[json-db] 'load_db' call \n");
#
#    try:
#        with open(filename, "r") as myfile:
#
##            print(myfile)
#
#            try:
#                db = json.load(myfile)
#                if not db:      # is_empty(db):
#                    raise Exception('Database is empty')        #DatabaseEmptyWarning('Database is empty')
#
#            except json.JSONDecodeError as err:
#                print("\n# <Exception> ", err.args[0], "\n")
#            except Exception as wrn:
#                print(wrn)
#            except:
#                print("\n# <Exception> ", "Unexpected error:", sys.exc_info(), "\n#")
#            finally:
##                print("\n[json-db] 'json_load_db' exit \nDataBase: ", db);
#                pass
#
#    except FileNotFoundError as err:
#        print("\n# <Exception> ", err, "\n")
#
#    return db
#
#
#
#def save_db(json_file, db):
#
##    print("\n[json-db] 'save_db' call \n");
#
#    with open(json_file,"w") as myfile:
##        print(myfile, "my file open w")
#
#        # Convert json to string
#        f = json.dumps(db, indent=4, sort_keys=True, cls=ObjectEncoder)
##        f = json.dumps(db, indent=4, sort_keys=True, default=ObjectEncoder().default)
##        print(f)
##        print("json dump")
#
#        # save into file
#        myfile.write(f)
#
#
#
#class ObjectEncoder(json.JSONEncoder):
#    def default(self, obj):
#        if isinstance(obj, (datetime.datetime, datetime.date)):
#            return obj.isoformat()
#        elif hasattr(obj, "to_dict"):
#            return obj.to_dict()
#
#
#        return json.JSONEncoder.default(self, obj)



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


#------------------------------------------------------------------------------

    # Init. model
    game_mdl = ZGame()
    game_mdl.init_playground()


    # Init. GUI
    pygame.init()

    pygame.key.set_repeat(400, 30)


    # Init. assets
    main_win = pygame.display.set_mode((480, 640))       # , pg_const.RESIZABLE

#    playground_view = main_win

    playground_view = pygame.image.load("background.jpg").convert()
#    playground_view.blit(background_surf, (0,0))

    wall_surf = pygame.image.load("structures.png").convert()
    wall_surf = pygame.transform.scale(wall_surf, (832,256))

    # Crop an element
    wall_top_left_surf = pygame.transform.chop(
            pygame.transform.chop(wall_surf, (64,64,wall_surf.get_width()-64,wall_surf.get_height()-64)),
            (0,0,32,32))
    print(wall_top_left_surf)
    wall_top_left_pos = wall_top_left_surf.get_rect()
    print(wall_top_left_pos)

    for row_idx, row in enumerate(game_mdl.playground):

        for sprite_idx, sprite in enumerate(row):

            if sprite == 'w':

                playground_view.blit(wall_top_left_surf, (sprite_idx*32,row_idx*32))



    main_win.blit(playground_view, playground_view.get_rect())




#    wall_top_left_pos = wall_top_left_surf.get_rect().move(50,50)
#    main_win.blit(wall_top_left_surf, wall_top_left_pos)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,1*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,2*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,3*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,4*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,5*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)
#    wall_top_left_pos = wall_top_left_pos.move(0,6*64)
#    playground_view.blit(wall_top_left_surf, wall_top_left_pos)


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
#    playground_view.blit(guard_surf, guard_pos)

#    main_win.blit(playground_view, playground_view.get_rect())

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
#        playground_view.blit(wall_top_left_surf, wall_top_left_pos)

#        print(hero_pos)

        main_win.blit(playground_view, playground_view.get_rect())
        main_win.blit(hero_surf, hero_pos)
        main_win.blit(guard_surf, guard_pos)

        pygame.display.flip()




