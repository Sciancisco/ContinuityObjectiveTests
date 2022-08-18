import logging
import pickle
import time

from bioptim import OdeSolver, Solver

from prepare_ocp import prepare_ocp_first_pass, prepare_ocp_second_pass


def test_constraint(
    biorbd_model_path: str,
    final_time: float,
    n_shooting: int,
    x_bounds,
    u_bounds,
    x_init,
    u_init,
    i,
    max_iteration,
    sol_dir,
    ode_solver: OdeSolver = OdeSolver.RK4(),
    n_threads: int = 1,
):
    logging.info(f"Running constraint test {i}...")
    ocp = prepare_ocp_first_pass(
        biorbd_model_path,
        final_time,
        n_shooting,
        x_bounds,
        u_bounds,
        x_init,
        u_init,
        weight=None,
        ode_solver=ode_solver,
        n_threads=n_threads,
    )
    solver = Solver.IPOPT()
    solver.set_maximum_iterations(max_iteration)
    sol = ocp.solve(solver)
    del sol.ocp

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = "constraint-{sol_index}-{timestamp}.pickle".format(sol_index=i, timestamp=timestamp)
    try:
        with open(sol_dir + filename, "wb") as f:
            pickle.dump(sol, f)
        logging.info(f"Saved solution {i} to '{sol_dir + filename}'.")
    except:
        logging.exception(f"Error when saving solution {i} to '{sol_dir + filename}'.")

    logging.info("Done constraint tests.")


def test_objective(
    biorbd_model_path: str,
    final_time: float,
    n_shooting: int,
    x_bounds,
    u_bounds,
    x_init,
    u_init,
    i,
    max_iteration_first,
    max_iteration_second,
    weight,
    sol_dir,
    ode_solver: OdeSolver = OdeSolver.RK4(),
    n_threads: int = 1,
):
    logging.info(f"Running objective test {i} with weight={weight} and max_iteration_first={max_iteration_first}...")
    start = time.time()
    ocp = prepare_ocp_first_pass(
        biorbd_model_path,
        final_time,
        n_shooting,
        x_bounds,
        u_bounds,
        x_init,
        u_init,
        weight,
        ode_solver=ode_solver,
        n_threads=n_threads,
    )
    solver = Solver.IPOPT()
    solver.set_maximum_iterations(max_iteration_first)
    sol1 = ocp.solve(solver)
    del sol1.ocp

    ocp = prepare_ocp_second_pass(biorbd_model_path, x_bounds, u_bounds, sol1, n_threads=n_threads)
    solver = Solver.IPOPT()
    solver.set_maximum_iterations(max_iteration_second)
    sol2 = ocp.solve(solver)
    del sol2.ocp
    stop = time.time()

    sol2.total_time = stop - start

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = "objective-initial-{sol_index}-{weight}-{max_iters}-{timestamp}.pickle".format(
        sol_index=i, weight=weight, max_iters=max_iteration_first, timestamp=timestamp
    )
    try:
        with open(sol_dir + filename, "wb") as f:
            pickle.dump(sol1, f)
        logging.info(f"Saved solution {i} to '{sol_dir + filename}'.")
    except:
        logging.exception(f"Error when saving solution {i} to '{sol_dir + filename}'.")

    filename = "objective-final-{sol_index}-{weight}-{max_iters}-{timestamp}.pickle".format(
        sol_index=i, weight=weight, max_iters=max_iteration_first, timestamp=timestamp
    )
    try:
        with open(sol_dir + filename, "wb") as f:
            pickle.dump(sol2, f)
        logging.info(f"Saved solution {i} to '{sol_dir + filename}'.")
    except:
        logging.exception(f"Error when saving solution {i} to '{sol_dir + filename}'.")
