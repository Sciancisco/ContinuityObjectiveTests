import numpy as np
from matplotlib import pyplot as plt
import os
import pickle

from functions import *


filenames = os.listdir(".")
solutions = [*map(load_sol, filenames)]

status = np.array([*map(extract_status, solutions)])
convergence_rate = len(status[status == 0]) / len(status)

opt_times = np.array([*map(extract_opt_time, solutions)])[status == 0]
iterations = np.array([*map(extract_iteration, solutions)])[status == 0]
#qs = np.array([*map(extract_q, solutions)])[status == 0]
#qdots = np.array([*map(extract_qdot, solutions)])[status == 0]
#taus = np.array([*map(extract_tau, solutions)])[status == 0]
costs = np.array([*map(extract_cost, solutions)])[status == 0]

print(f"Temps {np.mean(opt_times):.0f} std:{np.std(opt_times):.0f}")
print(f"Iterations {np.mean(iterations):.0f} std:{np.std(iterations):.0f}")
print(f"Cost {np.mean(costs):.5f} std:{np.std(costs):.5f}")
print(f"Convergence rate {convergence_rate*100}%")

