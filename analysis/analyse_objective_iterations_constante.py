import numpy as np
from matplotlib import pyplot as plt
import os

from functions import *


filenames = [*filter(lambda s: "final" in s, os.listdir("."))]
i1Knames = filter(lambda s: s.split("-")[3] == "1000.0", filenames)
i1Mnames = filter(lambda s: s.split("-")[3] == "1000000.0", filenames)
i1Gnames = filter(lambda s: s.split("-")[3] == "1000000000.0", filenames)

solutions1K = [*map(load_sol, i1Knames)]
solutions1M = [*map(load_sol, i1Mnames)]
solutions1G = [*map(load_sol, i1Gnames)]

status1K = np.array([*map(extract_status, solutions1K)])
status1M = np.array([*map(extract_status, solutions1M)])
status1G = np.array([*map(extract_status, solutions1G)])

conv1K = len(status1K[status1K == 0]) / len(status1K)
conv1M = len(status1M[status1M == 0]) / len(status1M)
conv1G = len(status1G[status1G == 0]) / len(status1G)

print("Taux de convergence")
print(f"1K \t{conv1K*100:.2f}%")
print(f"1M \t{conv1M*100:.2f}%")
print(f"1G \t{conv1G*100:.2f}%")
print()
print("Les resultats suivants sont pour les optimiations ayant converge.")
print()


opt_times1K = np.array([*map(extract_opt_time, solutions1K)])[status1K == 0]
opt_times1M = np.array([*map(extract_opt_time, solutions1M)])[status1M == 0]
opt_times1G = np.array([*map(extract_opt_time, solutions1G)])[status1G == 0]
topt1K = np.mean(opt_times1K)
sigtopt1K = np.std(opt_times1K)
topt1M = np.mean(opt_times1M)
sigtopt1M = np.std(opt_times1M)
topt1G = np.mean(opt_times1G)
sigtopt1G = np.std(opt_times1G)

print("Temps d'optimisation final")
print(f"1K \t{topt1K:.2f} +/- {sigtopt1K:.2f} s")
print(f"1M \t{topt1M:.2f} +/- {sigtopt1M:.2f} s")
print(f"1G \t{topt1G:.2f} +/- {sigtopt1G:.2f} s")
print()


total_times1K = np.array([*map(extract_total_time, solutions1K)])[status1K == 0]
total_times1M = np.array([*map(extract_total_time, solutions1M)])[status1M == 0]
total_times1G = np.array([*map(extract_total_time, solutions1G)])[status1G == 0]
ttot1K = np.mean(total_times1K)
sigttot1K = np.std(total_times1K)
ttot1M = np.mean(total_times1M)
sigttot1M = np.std(total_times1M)
ttot1G = np.mean(total_times1G)
sigttot1G = np.std(total_times1G)

print("Temps d'optimisation total (initial + final)")
print(f"1K \t{ttot1K:.2f} +/- {sigttot1K:.2f} s")
print(f"1M \t{ttot1M:.2f} +/- {sigttot1M:.2f} s")
print(f"1G \t{ttot1G:.2f} +/- {sigttot1G:.2f} s")
print()


iterations1K = np.array([*map(extract_iteration, solutions1K)])[status1K == 0]
iterations1M = np.array([*map(extract_iteration, solutions1M)])[status1M == 0]
iterations1G = np.array([*map(extract_iteration, solutions1G)])[status1G == 0]
it1K = np.mean(iterations1K)
sigit1K = np.std(iterations1K)
it1M = np.mean(iterations1M)
sigit1M = np.std(iterations1M)
it1G = np.mean(iterations1G)
sigit1G = np.std(iterations1G)

print("Nombre d'iterations pour l'optimisation final")
print(f"1K \t{it1K:.2f} +/- {sigit1K:.2f} it.")
print(f"1M \t{it1M:.2f} +/- {sigit1M:.2f} it.")
print(f"1G \t{it1G:.2f} +/- {sigit1G:.2f} it.")
print()


costs1K = np.array([*map(extract_cost, solutions1K)])[status1K == 0]
costs1M = np.array([*map(extract_cost, solutions1M)])[status1M == 0]
costs1G = np.array([*map(extract_cost, solutions1G)])[status1G == 0]
cost1K = np.mean(costs1K)
sigcost1K = np.std(costs1K)
cost1M = np.mean(costs1M)
sigcost1M = np.std(costs1M)
cost1G = np.mean(costs1G)
sigcost1G = np.std(costs1G)

print("Cout pour l'optimisation final")
print(f"1K \t{cost1K:.2f} +/- {sigcost1K:.2f}")
print(f"1M \t{cost1M:.2f} +/- {sigcost1M:.2f}")
print(f"1G \t{cost1G:.2f} +/- {sigcost1G:.2f}")
print()