# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:24:43 2023

@author: Jashan
"""
import time
from LP_functions import *

def main():
    pool_a = Pool(100000, 20)
    pool_b = Pool(50000, 9)
    pool_c = Pool(200000, 40)
    pool_d = Pool(100000, 22)
    print("\\\\\\\\\\")
    print("relative price pool_a: " + str(pool_a.get_relative_price()))
    print("relative price pool_b: " + str(pool_b.get_relative_price()))
    print("relative price pool_c: " + str(pool_c.get_relative_price()))
    print("relative price pool_d: " + str(pool_d.get_relative_price()))
    print("\\\\\\\\\\")
    
    start = time.time()
    
    for loops in range(100):
        print("\n\nFIRST EXAMPLE: ")
        print("First Pool = pool_a  || Second Pool = pool_b")
        calculate_arbitrage_eth(pool_a, pool_b)
        print("\n\nSECOND EXAMPLE: ")
        print("First Pool = pool_c  || Second Pool = pool_d")
        calculate_arbitrage_eth(pool_c, pool_d)
    end = time.time()
    
    print("Time Taken = " + str(end-start))

if __name__ == "__main__":
    main()