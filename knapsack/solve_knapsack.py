'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’
The goal is to get the maximum profit out of the knapsack items.
Each item can only be selected once, as we don’t have multiple quantities of any item.

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
'''



def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return solve_knapsack_recursive(profits, weights, capacity, 0, 0, dp)


def solve_knapsack_recursive(profits, weights, capacity, index, profit, dp):
    if capacity==0:
        return profit
    if capacity<0 or index>=len(weights):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    dp[index][capacity] =\
        max(solve_knapsack_recursive(profits, weights, capacity-weights[index], index+1, profit+profits[index], dp),
               solve_knapsack_recursive(profits, weights, capacity, index+1, profit, dp))

    return dp[index][capacity]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)) # 17
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)) # 22


main()



