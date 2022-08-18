import numpy as np
from matplotlib import pyplot as plt
import os

from functions import *


filenames = [*filter(lambda s: "final" in s, os.listdir("."))]
i100names = filter(lambda s: s.split("-")[4] == "100", filenames)
i1000names = filter(lambda s: s.split("-")[4] == "1000", filenames)
i10000names = filter(lambda s: s.split("-")[4] == "10000", filenames)

solutions100 = [*map(load_sol, i100names)]
solutions1000 = [*map(load_sol, i1000names)]
solutions10000 = [*map(load_sol, i10000names)]

status100 = np.array([*map(extract_status, solutions100)])
status1000 = np.array([*map(extract_status, solutions1000)])
status10000 = np.array([*map(extract_status, solutions10000)])

conv100 = len(status100[status100 == 0]) / len(status100)
conv1000 = len(status1000[status1000 == 0]) / len(status1000)
conv10000 = len(status10000[status10000 == 0]) / len(status10000)

print("Taux de convergence")
print(f"100 iterations\t\t{conv100*100:.2f}%")
print(f"1000 iterations\t\t{conv1000*100:.2f}%")
print(f"10000 iterations\t{conv10000*100:.2f}%")
print()
print("Les resultats suivants sont pour les optimiations ayant converge.")
print()


opt_times100 = np.array([*map(extract_opt_time, solutions100)])[status100 == 0]
opt_times1000 = np.array([*map(extract_opt_time, solutions1000)])[status1000 == 0]
opt_times10000 = np.array([*map(extract_opt_time, solutions10000)])[status10000 == 0]
topt100 = np.mean(opt_times100)
sigtopt100 = np.std(opt_times100)
topt1000 = np.mean(opt_times1000)
sigtopt1000 = np.std(opt_times1000)
topt10000 = np.mean(opt_times10000)
sigtopt10000 = np.std(opt_times10000)

print("Temps d'optimisation final")
print(f"100 iterations\t\t{topt100:.2f} +/- {sigtopt100:.2f} s")
print(f"1000 iterations\t\t{topt1000:.2f} +/- {sigtopt1000:.2f} s")
print(f"10000 iterations\t{topt10000:.2f} +/- {sigtopt10000:.2f} s")
print()


total_times100 = np.array([*map(extract_total_time, solutions100)])[status100 == 0]
total_times1000 = np.array([*map(extract_total_time, solutions1000)])[status1000 == 0]
total_times10000 = np.array([*map(extract_total_time, solutions10000)])[status10000 == 0]
ttot100 = np.mean(total_times100)
sigttot100 = np.std(total_times100)
ttot1000 = np.mean(total_times1000)
sigttot1000 = np.std(total_times1000)
ttot10000 = np.mean(total_times10000)
sigttot10000 = np.std(total_times10000)

print("Temps d'optimisation total (initial + final)")
print(f"100 iterations\t\t{ttot100:.2f} +/- {sigttot100:.2f} s")
print(f"1000 iterations\t\t{ttot1000:.2f} +/- {sigttot1000:.2f} s")
print(f"10000 iterations\t{ttot10000:.2f} +/- {sigttot10000:.2f} s")
print()


iterations100 = np.array([*map(extract_iteration, solutions100)])[status100 == 0]
iterations1000 = np.array([*map(extract_iteration, solutions1000)])[status1000 == 0]
iterations10000 = np.array([*map(extract_iteration, solutions10000)])[status10000 == 0]
it100 = np.mean(iterations100)
sigit100 = np.std(iterations100)
it1000 = np.mean(iterations1000)
sigit1000 = np.std(iterations1000)
it10000 = np.mean(iterations10000)
sigit10000 = np.std(iterations10000)

print("Nombre d'iterations pour l'optimisation final")
print(f"100 iterations\t\t{it100:.2f} +/- {sigit100:.2f} it.")
print(f"1000 iterations\t\t{it1000:.2f} +/- {sigit1000:.2f} it.")
print(f"10000 iterations\t{it10000:.2f} +/- {sigit10000:.2f} it.")
print()


costs100 = np.array([*map(extract_cost, solutions100)])[status100 == 0]
costs1000 = np.array([*map(extract_cost, solutions1000)])[status1000 == 0]
costs10000 = np.array([*map(extract_cost, solutions10000)])[status10000 == 0]
cost100 = np.mean(costs100)
sigcost100 = np.std(costs100)
cost1000 = np.mean(costs1000)
sigcost1000 = np.std(costs1000)
cost10000 = np.mean(costs10000)
sigcost10000 = np.std(costs10000)

print("Cout pour l'optimisation final")
print(f"100 iterations\t\t{cost100:.2f} +/- {sigcost100:.2f}")
print(f"1000 iterations\t\t{cost1000:.2f} +/- {sigcost1000:.2f}")
print(f"10000 iterations\t{cost10000:.2f} +/- {sigcost10000:.2f}")
print()