#!/usr/bin/env python3


def step1(ll):
    
    gamma = ''
    epsilon = ''

    for bit in range(len(ll[0])):
        sumof0 = sum(number[bit] == '0' for number in ll)
        sumof1 = sum(number[bit] == '1' for number in ll)
        if sumof0 > sumof1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
        
    return int(gamma, 2) * int(epsilon, 2)
        
    
def step2(ll):
    return 0
