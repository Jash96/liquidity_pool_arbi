"""
Created on Sun Mar 26 19:50:50 2023

@author: Jashan
"""

import sympy as sp # in-built into Python3 existing libraries, no need to pip-install
import copy # to allow copying of the original pools without changing their values when calculating arb

class Pool: # DAI/ETH Pool
    def __init__(self, dai: float, eth:float, fee: float = 0.003):
        self.dai = dai
        self.eth = eth
        self.k = dai * eth
        self.fee = fee
        
    def add_liquidity(self, dai: float, eth: float):
        self.dai += dai
        self.eth += eth
        self.k = self.dai * self.eth

    def remove_liquidity(self, dai: float, eth: float):
        self.dai -= dai
        self.eth -= eth
        self.k = self.dai * self.eth
    
    def get_relative_price(self):
        return self.eth / self.dai
    
    def print_LP_status(self):
        print("new DAI reserve: " + str(self.dai) )
        print("new ETH reserve: " + str(self.eth) )
        print("relative_price: " + str(self.get_relative_price() ) )
        print("K: " + str(self.k) )
        

def swap(pool: Pool, amount: float, from_token: str, to_token: str) -> float: # Knowing Input Amounts
    # Given INPUT DAI, return RECEIVED ETH (after fees)
    if from_token == 'dai' and to_token == 'eth':
#         print("Swapping " + str(amount) + " DAI to ETH...")
        eth_received = ((1 - pool.fee) * pool.eth * amount)/(pool.dai + (1 - pool.fee) * amount)
        pool.add_liquidity(amount, 0)
        pool.remove_liquidity(0, eth_received)
#         print(str(amount) + " DAI swapped to " + str(eth_received) + " ETH received")
        return eth_received
    
    # Given INPUT ETH, return RECEIVED DAI (after fees)
    elif from_token == 'eth' and to_token == 'dai':
#         print("Swapping " + str(amount) + " ETH to DAI...")
        dai_received = ((1 - pool.fee) * pool.dai * amount)/(pool.eth + (1 - pool.fee) * amount)
        pool.add_liquidity(0, amount)
        pool.remove_liquidity(dai_received, 0)
#         print(str(amount) + " ETH swapped to " + str(dai_received) + " DAI received")
        return dai_received
    # Error message
    else:
        raise ValueError("Invalid Token Pair. :( ")
        
def swap_getInput(pool: Pool, from_token: str, to_token: str, amountOut: float): # Knowing Output needed
    # Given OUTPUT ETH needed, calculate INPUT DAI required
    if from_token == 'dai' and to_token == 'eth':
#         print("To get " + str(amountOut) + " of ETH...")
        dai_needed = (pool.dai * amountOut) / ((1 - pool.fee) * (pool.eth - amountOut))
#         print("You will need " + str(dai_needed) + " DAI")
        return dai_needed
    
    # Given OUTPUT DAI needed, calculate INPUT ETH required
    if from_token == 'eth' and to_token == 'dai':
#         print("To get " + str(amountOut) + " of DAI...")
        eth_needed = (pool.eth * amountOut) / ((1 - pool.fee) * (pool.dai - amountOut))
#         print("You will need " + str(eth_needed) + " ETH")
        return eth_needed
    
    
def optimal_dai(expensive_pool: Pool, cheap_pool: Pool) -> float:
    rel_e = expensive_pool.get_relative_price()
    rel_c = cheap_pool.get_relative_price()
    dai_e, eth_e = expensive_pool.dai, expensive_pool.eth
    dai_c, eth_c = cheap_pool.dai, cheap_pool.eth
    x = sp.symbols('x')
    eq = sp.Eq((eth_c + rel_c * x)/(dai_c - x), (eth_e - rel_e * x)/(dai_e + x))
    # Solve for x
    sol = sp.solve(eq, x)
    # Print the solution
#     print("x =", sol)
    
    valid_solutions = []
    for s in sol:
        if s <= dai_c:
            valid_solutions.append(s)
    # Print the valid solution(s)
    if len(valid_solutions) == 1:
#         print("x =", valid_solutions[0])
        return valid_solutions[0]
    elif len(valid_solutions) > 1:
        print("More than 1 solution found")
    else:
        print("No valid solution found.")
        
def calculate_arbitrage_eth(pool_a: Pool, pool_b: Pool):
    rel_a = pool_a.get_relative_price()
    rel_b = pool_b.get_relative_price()
    
    temp_a = copy.deepcopy(pool_a)
    temp_b = copy.deepcopy(pool_b)
    
    print("\n----------------------------------------------------------------------------------------")
    print("Current relative prices of the 2 pools: " + str(rel_a) + " and " + str(rel_b))
#     print(rel_a, rel_b)
    if rel_a > rel_b: # Buy cheaper DAI from pool_b
        print("\nBuy " + str(optimal_dai(temp_a, temp_b)) + " DAI from second pool and sell to first pool")
        eth_req = swap_getInput(temp_b, 'eth', 'dai', optimal_dai(temp_a, temp_b))
        dai_swapped = swap(temp_b, eth_req, 'eth', 'dai')
        eth_earned = swap(temp_a, dai_swapped, 'dai', 'eth')
        print("ETH required for arbitrage: " + str(eth_req))
        print("ETH earned after arbitrage: " + str(eth_earned))
        print("\nProfit after arbitrage in ETH: \n" + str(eth_earned - eth_req))
        print("\nEnding relative prices for both pools: " + str(temp_a.get_relative_price()) + " and " + str(temp_b.get_relative_price()))
        print("+++++++++++++++++++++++++++++++++++++++++")
        return eth_req, eth_earned - eth_req
    elif rel_a < rel_b:
        print("\nBuy " + str(optimal_dai(temp_b, temp_a)) + " DAI from first pool and sell to second pool")
        eth_req = swap_getInput(temp_a, 'eth', 'dai', optimal_dai(temp_b, temp_a))
        dai_swapped = swap(temp_a, eth_req, 'eth', 'dai')
        eth_earned = swap(temp_b, dai_swapped, 'dai', 'eth')
        print("ETH required for arbitrage: " + str(eth_req))
        print("ETH earned after arbitrage: " + str(eth_earned))
        print("\nProfit after arbitrage in ETH: \n" + str(eth_earned - eth_req))
        print("\nEnding relative prices for both pools: " + str(temp_a.get_relative_price()) + " and " + str(temp_b.get_relative_price()))
        print("+++++++++++++++++++++++++++++++++++++++++")
        return eth_req, eth_earned - eth_req
    else:
        print("No arbitrage opportunity present :( ")

