#!/usr/bin/env python3


def step1(bin_list):
    
    gamma = ''
    epsilon = ''

    for bit in range(len(bin_list[0])):
        sum_of_0 = sum(number[bit] == '0' for number in bin_list)
        sum_of_1 = sum(number[bit] == '1' for number in bin_list)

        gamma += '0' if (sum_of_0 > sum_of_1) else '1'
        epsilon += '1' if (sum_of_0 > sum_of_1) else '0'

        
    return int(gamma, 2) * int(epsilon, 2)
        
    
def step2(bin_list):
    return 0


with open('data.txt', 'r') as file:
    data = file.read().splitlines()
print(step1(data))
