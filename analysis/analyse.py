import argparse
import os

from dataframe import DataFrame
from functions import *

parser = argparse.ArgumentParser("Analyse data.")
parser.add_argument("solution_dir", type=str, help="directory containing solutions")
args = parser.parse_args()


def extract_keys(filename):
    filename = filename.split("-")

    if filename[0] == "objective":
        type_, var, phase, case, weight, iter_ = filename[:6]
        case = int(case)
        if weight == "1000.0":
            weight = "1K"
        elif weight == "1000000.0":
            weight = "1M"
        elif weight == "1000000000.0":
            weight = "1G"
        iter_ = int(iter_)
        return dict(type=type_, var=var, phase=phase, case=case, weight=weight, iter=iter_)

    elif filename[0] == "constraint":
        type_, var, phase, case, weight, iter_ = filename[0], None, None, filename[1], None, None
        return dict(type=type_, var=var, phase=phase, case=case, weight=weight, iter=iter_)


df = DataFrame("type", "var", "phase", "case", "weight", "iter")

filenames = filter(lambda filename: ".pickle" in filename, os.listdir(args.solution_dir))

solutions = map(load_sol, filenames)
keys = map(extract_keys, filenames)

for k, sol in zip(keys, solutions):
    df.add(sol, **k)

