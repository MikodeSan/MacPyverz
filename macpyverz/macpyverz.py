# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:42 2019

@author: mtt
"""

# import sys
# import os
import argparse
import logging as lg

from view import ZView


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
#    print('Enable log', lg.info)
    lg.debug('Enable log')

#    if args.extension == 'xml':
#        print('xml analysis')
#    elif args.extension == 'csv':
#        print('csv analysis')
#    else:
#        print('unknown file extension')

    lg.info('Start Application')


    view = ZView(lg)
    view.refresh_playground()
    view.run()

#------------------------------------------------------------------------------






