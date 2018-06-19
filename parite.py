#! /usr/bin/env python3
# coding: utf-8

import os
import analysis.csv as c_an
import analysis.xml as x_an
import argparse
import logging as lg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


lg.basicConfig(level = lg.DEBUG)

class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party = False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data",data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

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
    print("##### All parties #####")
    launch_analysis(datafile,False)
    print("##### By party #####")
    launch_analysis(datafile, True)


if __name__ == "__main__":
    main()