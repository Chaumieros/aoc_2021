#!/usr/bin/env python3

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
    current_sum = 0
    increased_count = 0
    offset = 1

    with open('data.txt', 'r') as f:
        lines = list(map(int, f.read().splitlines()))

        for (index , depth) in enumerate(lines[offset:]):
            index = index + offset
            current_sum = sum(lines[index:index+3])
            previous_sum = sum(lines[index-1:index+2])
            if current_sum > previous_sum:
                increased_count += 1
   

        print(f"There are {increased_count} sums that are larger than the previous sum")    

step2()