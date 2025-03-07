# Knapsack Problem in Python
# The Knapsack Problem is to optimize the content of the Knapsack
# Trying to maximize the value with a limited capacity
import time
from itertools import combinations


items = [
    {"weight": 10, "value": 60},
    {"weight": 20, "value": 100},
    {"weight": 30, "value": 120},
    {"weight": 5, "value": 30},
    {"weight": 15, "value": 80},
    {"weight": 25, "value": 90},
    {"weight": 12, "value": 50},
    {"weight": 7, "value": 40},
    {"weight": 18, "value": 75},
    {"weight": 22, "value": 110},
    {"weight": 8, "value": 35},
    {"weight": 14, "value": 70},
    {"weight": 11, "value": 45},
    {"weight": 16, "value": 85},
]

capacity = 50

def knapsack_brute_force(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = None
    used_capacity = None
    runtime_counter = 0

    for r in range(n + 1):
        for combination in combinations(items, r):
            runtime_counter += 1
            total_weight = sum(item["weight"] for item in combination)
            total_value = sum(item["value"] for item in combination)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combination
                used_capacity = total_weight
                

    return best_value, best_combination, used_capacity


def knapsack_greedy_function(items, capacity):
    items_sorted = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)
    total_value = 0
    total_weight = 0
    chosen_items = []

    for item in items_sorted:
        if total_weight + item["weight"] <= capacity:
            chosen_items.append(item)
            total_weight += item["weight"]
            total_value += item["value"]

    return total_value, chosen_items, total_weight



def knapsack_dynamic_function(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1]["weight"] <= w:
                dp[i][w] = max(items[i-1]["value"] + dp[i-1][w-items[i-1]["weight"]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    chosen_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(items[i-1])
            w -= items[i-1]["weight"]

    total_value = dp[n][capacity]
    return total_value, chosen_items

start = time.perf_counter()
print(knapsack_brute_force(items, capacity))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(knapsack_greedy_function(items, capacity))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(knapsack_dynamic_function(items, capacity))
end = time.perf_counter()
print(end-start)