#! /usr/bin/env python3
# coding: utf-8

import os

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)

    with open(path_to_file, "r") as f:
        preview = f.readline()

    print("Check the preview : {}".format(preview))

if __name__ == "__main__":
    launch_analysis("SyceronBrut.xml")
