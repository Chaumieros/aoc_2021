#!/usr/bin/env python3

from day3 import step1, step2

def test():
    values = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    assert step1(values) == 198
    print("Step 1 ok")

test()