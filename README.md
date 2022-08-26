# ObstacleWorkAround

## Experiments breakdown

100 noized initial guess where generated procedurally with `np.random.seed(42)`, a popular seed may I say.

### Constraints

Ran the OCP the classic way, 10_000 iterations max.

### Objectives

Ran the OCP in two phases. Phase 1: try to solve using Continuity as an objective and Phase 2: solve the classic way using the solution from phase 1 as the initial guess.
Three run were tested:
1. with variable number of max iterations (100, 1000, 10_000) in phase 1 with the same weight for each (1_000_000).
2. with variable weight (1000, 1_000_000, 1_000_000_000) in phase 1 with the same number of max iterations (10_000).
3. with what seemed an optimal combination after preliminary analysis (weight 1_000_000_000 for 1000 iterations max in phase 1).

