#!/usr/bin/python3

def get_movements(l):
    #return an array of tuples as (movement : stf , value : str) for each line of the list l.

    return [tuple(ligne.split()) for ligne in l]


    
def step1(l):
    #return position * depth

    x = 0
    y = 0
    movements = get_movements(l)

    for movement, value in movements: 
        if movement == "forward":
            x += int(value)
        elif movement == "up":
            y -= int(value)
        else:
            y += int(value)

    return x * y 

def step2(l):

    x = 0
    y = 0
    aim = 0
    movements = get_movements(l)

    for movement, value in movements:
        if movement == "forward":
            x += int(value)
            y += int(value) * aim
        elif movement == "up":
            aim -= int(value)
        else:
            aim += int(value)
    
    return x * y 


with open('data.txt') as file:
    data = file.read().splitlines()
    print(f"Step1 : Horizontal position * depth = {step1(data)}")
    print(f"Step2 : Horizontal position * depth = {step2(data)}")