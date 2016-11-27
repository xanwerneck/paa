#!/bin/env bash

rm -rf instances_solutions
mkdir -p instances_solutions
for input in instances/Data*; do
    basename=${input%.*}
    output_basename=instances_solutions/${basename#*/}
    for q in `seq 1 3`; do
        output=${output_basename}_out_question${q}.txt
        cmd="python3 knapsack.py ${input} ${q} > ${output}"
        eval ${cmd} &
        if [ $? -ne 0 ]; then
            echo "error!"
            exit 1
        fi
    done
done
wait
echo "done!"

