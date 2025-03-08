### 🌊 Knapsack Problem  

#### 🏆 Optimizing Value with Limited Capacity  

The **Knapsack Problem** is a classic combinatorial optimization problem that involves selecting a set of items, each with a given weight and value, to maximize the total value without exceeding a fixed weight capacity. It has widespread applications in finance, logistics, and resource allocation.  

This project implements **three different algorithms** to solve the Knapsack Problem:  

- **Brute Force Approach** (Exhaustive Search)  
- **Greedy Algorithm** (Heuristic-based selection)  
- **Dynamic Programming Algorithm** (Optimal substructure approach)  

By comparing the **runtime and efficiency** of these methods, we can determine which approach is best suited for different scenarios.  

---

## 🤔 What is the Knapsack Problem?  

The **Knapsack Problem** is defined as follows:  

> Given `n` items, each with a weight `w` and a value `v`, determine the subset of items that maximizes the total value while ensuring the total weight does not exceed a given capacity `C`.  

Mathematically, we want to maximize:  
\[
\sum v_i \quad \text{subject to} \quad \sum w_i \leq C
\]
where \( v_i \) and \( w_i \) are the value and weight of each selected item, respectively.  

### 🔥 Real-World Applications:  
- **Investment Portfolio Optimization:** Selecting stocks with maximum return under a budget.  
- **Cargo Loading:** Maximizing the value of goods transported in a truck or shipping container.  
- **Resource Allocation:** Assigning limited computational resources efficiently.  

---

## 🛠️ Brute Force Algorithm (Exhaustive Search)  

This approach **checks all possible combinations** of items to find the optimal solution. It guarantees the **best** solution but has an exponential time complexity **O(2ⁿ)**, making it impractical for large datasets.  

### Implementation:  
- Generate all subsets of items.  
- Compute the total weight and value for each subset.  
- Keep track of the best subset that fits within the capacity.  

**Pros:** ✅ Finds the optimal solution.  
**Cons:** ❌ Very slow for large inputs.  

---

## ⚡ Greedy Algorithm (Approximation)  

This approach **sorts items by their value-to-weight ratio** and picks items greedily until the capacity is full. While fast **O(n log n)**, it does not always provide the optimal solution.  

### Implementation:  
- Sort items by **value/weight** ratio.  
- Pick the most valuable item that fits in the remaining capacity.  

**Pros:** ✅ Fast and simple.  
**Cons:** ❌ May not find the optimal solution in all cases.  

---

## 🧮 Dynamic Programming Algorithm (Optimal Solution)  

This approach **uses a 2D table to store subproblem results**, ensuring we only compute values once. It runs in **O(n × C)** time, making it much more efficient than brute force for larger capacities.  

### Implementation:  
- Construct a **DP table** where `dp[i][w]` stores the best value for `i` items with weight limit `w`.  
- Use the recurrence relation:  
  \[
  dp[i][w] = \max(dp[i-1][w], v_i + dp[i-1][w - w_i])
  \]
- Backtrack to determine selected items.  

**Pros:** ✅ Finds the optimal solution efficiently.  
**Cons:** ❌ Slightly higher memory usage due to DP table.  

---

## 📊 Comparing Each Algorithm  

| Algorithm      | Time Complexity | Guarantees Optimal? | Suitable for Large Inputs? |
|---------------|----------------|----------------------|----------------------------|
| **Brute Force** | O(2ⁿ)           | ✅ Yes               | ❌ No (Too slow for large `n`) |
| **Greedy**     | O(n log n)      | ❌ No (Approximate)  | ✅ Yes (Fast for large `n`) |
| **Dynamic**    | O(n × C)        | ✅ Yes               | ✅ Yes (Efficient for large `C`) |

### 🔥 Performance Test Results  

Using a dataset of 14 items and a **capacity of 50**, the execution times were:  

- **Brute Force:** `0.0192s`
- **Greedy:** `1.4542s`
- **Dynamic:** `0.00024s`  

This confirms that **brute force is impractical for large problems**, while **dynamic programming offers the best balance of accuracy and efficiency**.  

---

## 🎯 Conclusion  

The **Knapsack Problem** is a fundamental optimization problem with real-world applications. This project implemented three solutions, demonstrating the trade-offs between **accuracy and efficiency**.  

- **Brute Force** ensures optimality but is impractical for large inputs.  
- **Greedy Algorithm** is fast but may not find the best solution.  
- **Dynamic Programming** balances speed and accuracy, making it the best choice for larger datasets.  

This project highlights how **algorithmic choices impact performance**, providing valuable insights for tackling optimization problems in real-world applications. 🚀  

---

