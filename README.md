# liquidity_pool_arbitrage assignment - (Jashan Thadani)
Create pools, make swaps, and calculate arbitrage potential

## Within the main file contains 5 files:

- LP_functions.py
- swap_method.py
- arbitrage_calculation_logic.py
- non_block_calculation.py
- testing_ground_arbitrage_uniswap.ipynb

## What each file contains with regardst to the test questions:

- To see the data structs of pool status and the implemented add_liquidity, remove_liquidity and swap functions that maintains the status data in memory, you will need to run 'LP_functions.py'
- To see the arbitrage calculation logic (excluding non-blocking mode) where you get the ETH amount needed for arbitrage and profit in ETH from the arbitrage, you will need to run the 'arbitrage_calculation_logic.py' Note: it repeats 2 arbitrages across 4 pools 100 times. To assess the correctness of each arbitrage, wait for it to run and see each output as the values.
- Test cases to simulate user's swap transactions can be accessed from 'swap_method.py'
- The non-blocking mode calculation attempt is in 'non_block_calculation.py' using threading
- Lastly, my initial working and testing grounds was done on a Jupyter notebook and all of this can be seen in the 'testing_ground_arbitrage_uniswap.ipynb'


## Steps to go through my code for the base questions:
- Run 'LP_functions.py' , 'arbitrage_calculation_logic.py' and 'swap_method.py' to ensure that the pool objects are created and that you are able to see simulated swaps as well as the arbitrage calculations

I was not able to fully solve the issue on how to trigger the calculations in non-blocking mode. However, I think I have figured out how to implement it but it would require re-factoring my pool functions to work in a multithreaded way. To elaborate, currently my "calculate_arbitrage_eth" function calls other functions like "swap", "swap_getInput", "optimal_dai" which are called in a blocking mode. To avoid this, I would need to change the way I call my functions. Alternatively, there is a method I could use using the Python library "asyncio" which would allow me to run processes in the background but I have not figured that out in the time constraint.



