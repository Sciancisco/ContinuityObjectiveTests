import numpy as np
from matplotlib import pyplot as plt
import os
import pickle

def load_sol(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def extract_opt_time(solution):
    return solution.solver_time_to_optimize


def extract_iteration(solution):
    return solution.iterations


def extract_status(solution):
    return solution.status


def extract_q(solution):
    return solution.states["q"]


def extract_qdot(solution):
    return solution.states["qdot"]


def extract_tau(solution):
    return solution.controls["tau"]


filenames = os.listdir(".")
solutions = [*map(load_sol, filenames)]

status = np.array([*map(extract_status, solutions)])
convergence_rate = len(status[status == 0]) / len(status)

opt_times = np.array([*map(extract_opt_time, solutions)])[status == 0]
iterations = np.array([*map(extract_iteration, solutions)])[status == 0]
qs = np.array([*map(extract_q, solutions)])[status == 0]
qdots = np.array([*map(extract_qdot, solutions)])[status == 0]
taus = np.array([*map(extract_tau, solutions)])[status == 0]

print(f"Temps {np.mean(opt_times):.0f} std:{np.std(opt_times):.0f}")
print(f"Iterations {np.mean(iterations):.0f} std:{np.std(iterations):.0f}")
print(f"Convergence rate {convergence_rate*100}%")

