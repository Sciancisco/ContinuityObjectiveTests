import argparse
import logging

import biorbd
from bioptim import Bounds, QAndQDotBounds, NoisedInitialGuess
import numpy as np

from tests import test_constraint, test_objective

logging.basicConfig(
    filename="ObstacleWorkAround.log", level=logging.INFO, format="%(asctime)s:%(levelname)s: %(message)s"
)

parser = argparse.ArgumentParser("Run test for a particular case.")
parser.add_argument("type", action="store", help="type of test (constraint or objective)")
parser.add_argument(
    "--iters1", action="store", required=True, type=int, help="maximum number of iterations allowed on first pass"
)
parser.add_argument(
    "--iters2", action="store", required=False, type=int, help="maximum number of iterations allowed on second pass"
)
parser.add_argument("--weight", action="store", required=False, type=float, help="weight of continuity objective")

args = parser.parse_args()


def prepare_x_bounds(biorbd_model):
    x_bounds = QAndQDotBounds(biorbd_model)
    x_bounds[:, 0] = 0

    return x_bounds


def prepare_u_bounds(biorbd_model):
    n_tau = biorbd_model.nbGeneralizedTorque()
    tau_min, tau_max = -300, 300
    u_bounds = Bounds([tau_min] * n_tau, [tau_max] * n_tau)
    u_bounds[1, :] = 0  # Prevent the model from actively rotating

    return u_bounds


seed = 42
np.random.seed(seed)
sol_dir = "solutions/"

biorbd_model_path = "models/pendulum_maze.bioMod"
biorbd_model = biorbd.Model(biorbd_model_path)
nb_q = biorbd_model.nbQ()
nb_qdot = biorbd_model.nbQdot()
nb_tau = biorbd_model.nbGeneralizedTorque()

n_shooting = 500
final_time = 5
n_threads = 4

x_bounds = prepare_x_bounds(biorbd_model)
u_bounds = prepare_u_bounds(biorbd_model)

x_inits = [
    NoisedInitialGuess([0] * (nb_q + nb_qdot), bounds=x_bounds, noise_magnitude=0.001, n_shooting=n_shooting)
    for _ in range(100)
]
u_inits = [
    NoisedInitialGuess([0] * nb_tau, bounds=u_bounds, noise_magnitude=0.01, n_shooting=n_shooting - 1)
    for _ in range(100)
]

if args.type == "objective":
    logging.info(
        f"Testing continuity objective "
        f"seed={seed} "
        f"final_time={final_time} "
        f"n_shooting={n_shooting} "
        f"iters1={args.iters1} "
        f"iters2={args.iters2} "
        f"weight={args.weight} "
        #f"n_threads={n_threads}..."
    )

    test_objective(
        biorbd_model_path,
        final_time,
        n_shooting,
        x_bounds,
        u_bounds,
        x_inits,
        u_inits,
        args.iters1,
        args.iters2,
        args.weight,
        sol_dir,
        #n_threads=n_threads,
    )

    logging.info("Done, Good Bye!")

elif args.type == "constraint":
    logging.info(
        f"Testing continuity constraint "
        f"seed={seed} "
        f"final_time={final_time} "
        f"n_shooting={n_shooting} "
        f"iters1={args.iters1} "
        #f"n_threads={n_threads}..."
    )

    test_constraint(
        biorbd_model_path,
        final_time,
        n_shooting,
        x_bounds,
        u_bounds,
        x_inits,
        u_inits,
        args.iters1,
        sol_dir,
        #n_threads=n_threads,
    )

    logging.info("Done, Good Bye!")

else:
    print("Invalid type.")
