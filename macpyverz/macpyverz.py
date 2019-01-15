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

#import pygame.mixer
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


ASSET_SIZE=32

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






