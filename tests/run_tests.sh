#!/bin/sh


# run constraint tests DONE
for ((n=0; n<100; n=n+1)); do
  python3 obstacle_work_around.py constraint  $n --iters1 10000
done

# run objective tests set weight
max_iters=(100 1000 10000)
for ((n=0; n<100; n=n+1)); do
  for max_iter in ${max_iters[*]}; do
    python3 obstacle_work_around.py objective $n --var varit --iters1 ${max_iter} --iters2 10000 --weight 1000000
  done
done

# run objective tests set iters
weights=(1000 1000000 1000000000)
for ((n=0; n<100; n=n+1)); do
  for weight in ${weights[*]}; do
    python3 obstacle_work_around.py objective $n --var varpoids --iters1 10000 --iters2 10000 --weight ${weight}
  done
done

# run objective tests optimal weight and iter
for ((n=0; n<100; n=n+1)); do
  python3 obstacle_work_around.py objective $n --var varopt --iters1 1000 --iters2 10000 --weight 1000000000
done