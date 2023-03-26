# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:59:56 2023

@author: Jashan
"""

from LP_functions import *

def main():
    
    # Pool (amount of DAI, amount of ETH)
    
    pool_x = Pool(100000, 20)
    pool_y = Pool(50000, 9)
    pool_z = Pool(2000, 2)
    
    # Examples status update and swap of each pool
    
        # EXAMPLE 1
    
    pool_x.print_LP_status()
    
    swap(pool_x, 5000, 'dai', 'eth')
    
    pool_x.print_LP_status()
    
    print("\n")
     
        # EXAMPLE 2
 
    pool_y.print_LP_status()
    
    swap(pool_y, 1, 'eth', 'dai')
    
    pool_y.print_LP_status()
    print("\n")
    
        # EXAMPLE 3
 
    pool_z.print_LP_status()
    
    swap(pool_z, 350, 'dai', 'eth')
    
    pool_z.print_LP_status()
    print("\n")
    
    
    
    
if __name__ == "__main__":
    main()