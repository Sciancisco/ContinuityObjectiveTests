import pickle


def load_sol(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def extract_opt_time(solution):
    return solution.solver_time_to_optimize


def extract_total_time(solution):
    return solution.total_time


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


def extract_cost(solution):
    return solution.cost
