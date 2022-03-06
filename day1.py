#!/usr/bin/env python3


from ast import increment_lineno
from os import defpath
from time import perf_counter


def step1():
    with open('data.txt', 'r') as f:
        
        previous_depth = 0
        depth = 0
        state = ""
        increased_count = 0 

        for line in f:
            depth = int(line)
            if previous_depth == 0:
                state="(N/A - no previous measurement)"
            elif depth > previous_depth:
                state="(increased)"
                increased_count += 1
            else:
                state="(decreased)"

            print(str(depth) + " " + str(state))
            previous_depth = depth
        

        print("There are " + str(increased_count) + " measurements that are larger than the previous measurements.")

def step2():

    previous_sum = 0
    sum = 0
    state = ""
    increased_count = 0

    with open('data.txt', 'r') as f:
        file_content = f.read()
        lines = file_content.splitlines()

        for (index , depth) in enumerate(lines[2:]):
            sum = int(lines[index+2]) + int(lines[index+1]) + int(lines[index])
            previous_sum = int(lines[index+1]) + int(lines[index]) + int(lines[index-1])

            if index == 0:
                state = "(N/A - no previous measurement)"
            elif sum > previous_sum:
                state = "Increased"
                increased_count += 1
            elif sum < previous_sum:
                state = "Decreased"
            elif sum == previous_sum:
                state="No change"
            
            print(f"{sum} {state}")

        print(f"there are {increased_count} sums that are larger than the previous sum")    

    
step2()
