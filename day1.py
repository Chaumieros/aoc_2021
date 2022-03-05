#!/usr/bin/env python3

from ast import increment_lineno


with open('data.txt', 'r') as f:
    
    line_count = 0
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
    

    print("There are " + str(increased_count) + " measurements taht are larger than the previous measurements.")



