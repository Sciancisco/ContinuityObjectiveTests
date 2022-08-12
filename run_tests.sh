#!/bin/sh

max_iters=(100 1000 10000)
weights=(1000 1000000 1000000000)

# run constraint tests
python3 obstacle_work_around.py constraint --iters1 10000

# run objective tests set weight
for max_iter in ${max_iters[*]}; do
  python3 obstacle_work_around.py objective --iters1 ${max_iter} --iters2 10000 --weight 1000000
done

# run objective tests set iters
for weight in ${}; do
  python3 obstacle_work_around.py objective --iters1 10000 --iters2 10000 --weight ${weight}
done
