#! /usr/bin/env python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an
import argparse
import logging as lg

lg.basicConfig(level = lg.DEBUG)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML ? """)
    parser.add_argument("-d", "--datafile", help="""CSV or XML file containing pueces of information about the members of parliament """)
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning("You must indicate a datafile !")
        else:
            try:
                if args.extension == "xml":
                    x_an.launch_analysis(datafile)
                elif args.extension == "csv":
                    # import pdb;pdb.set_trace() : DEBOGGER
                    c_an.launch_analysis(datafile)
            except FileNotFoundError as e:
                 lg.error(e)
            finally:
                lg.info('#################### Analysis is over ######################')
    except Warning as e:
        lg.warning(e)

if __name__ == "__main__":
    main()