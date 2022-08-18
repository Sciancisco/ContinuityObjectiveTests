import argparse
import os

from matplotlib import pyplot as plt

from dataframe import DataFrame
from extractors import *

parser = argparse.ArgumentParser("Analyse data.")
parser.add_argument("solution_dir", type=str, help="directory containing solutions")
args = parser.parse_args()

df = DataFrame("type", "var", "phase", "case", "weight", "iter")

filenames = [*filter(lambda filename: ".pickle" in filename, os.listdir(args.solution_dir))]

solutions = map(load_sol, filenames)
keys = map(extract_keys, filenames)

for k, sol in zip(keys, solutions):
    df.add(sol, **k)

constraint_summary = {}
constraints = df(type="constraint")
for constraint in constraints:
    constraint.integrate(keep_intermediate_points=True)
