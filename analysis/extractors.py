import pickle


def load_sol(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


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
        case = int(case)
        return dict(type=type_, var=var, phase=phase, case=case, weight=weight, iter=iter_)

    else:
        raise Exception(filename)


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
