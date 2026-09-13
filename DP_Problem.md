# Dynamic Programming Roadmap

A structured **60-problem Dynamic Programming roadmap**, progressing from basic 1D DP to advanced DP patterns.

---

## 🟢 Level 1 — DP Basics

**Focus:** 1D DP, recurrence, memoization → tabulation

| # | Problem | Main Concept |
|---:|---|---|
| 0 | Fibonacci Number | Basic DP |
| 1 | Climbing Stairs | 1D DP |
| 2 | Min Cost Climbing Stairs | 1D DP + minimum |
| 3 | House Robber | Take / Not Take |
| 4 | House Robber II | Circular DP |
| 5 | N-th Tribonacci Number | 1D DP |
| 6 | Decode Ways | DP + string |
| 7 | Maximum Subarray | DP / Kadane |

### ⭐ Must-master

**Climbing Stairs → House Robber → Decode Ways**

---

## 🟡 Level 2 — Grid DP

**Focus:** 2D state and movement

| # | Problem | Main Concept |
|---:|---|---|
| 8 | Unique Paths | Grid DP |
| 9 | Unique Paths II | Obstacles |
| 10 | Minimum Path Sum | Min-cost grid |
| 11 | Triangle | Bottom-up DP |
| 12 | Maximum Path Sum in Matrix | Multiple directions |
| 13 | Dungeon Game | Reverse DP |

### ⭐ Must-master

**Unique Paths → Minimum Path Sum → Dungeon Game**

---

## 🟡 Level 3 — Knapsack / Subset DP

This is **extremely important for interviews**.

**Focus:**
> "Take it or don't take it"

| # | Problem | Main Concept |
|---:|---|---|
| 14 | 0/1 Knapsack | Classic knapsack |
| 15 | Subset Sum | Boolean DP |
| 16 | Partition Equal Subset Sum | Subset DP |
| 17 | Target Sum | Knapsack transformation |
| 18 | Coin Change | Unbounded knapsack |
| 19 | Coin Change II | Counting combinations |
| 20 | Combination Sum IV | Counting permutations |
| 21 | Last Stone Weight II | Knapsack transformation |

### ⭐ Must-master

**0/1 Knapsack → Subset Sum → Partition Equal Subset Sum → Coin Change → Target Sum**

If you understand these, a huge number of DP problems become easier.

---

## 🟠 Level 4 — String DP

**Focus:** Comparing two strings / subsequences.

| # | Problem | Main Concept |
|---:|---|---|
| 22 | Longest Common Subsequence | 2D string DP |
| 23 | Longest Palindromic Subsequence | LCS / interval DP |
| 24 | Edit Distance | Insert / Delete / Replace |
| 25 | Delete Operation for Two Strings | LCS |
| 26 | Distinct Subsequences | Counting DP |
| 27 | Interleaving String | 2D state |
| 28 | Word Break | String + DP |
| 29 | Palindrome Partitioning II | Partition DP |

### ⭐ Must-master

**LCS → Edit Distance → Distinct Subsequences → Word Break**

---

## 🟠 Level 5 — LIS / Subsequence DP

**Focus:**
> "What is the best answer ending at index `i`?"

| # | Problem | Main Concept |
|---:|---|---|
| 30 | Longest Increasing Subsequence | Classic LIS |
| 31 | Number of Longest Increasing Subsequence | LIS + counting |
| 32 | Longest Divisible Subset | LIS pattern |
| 33 | Maximum Length of Pair Chain | LIS |
| 34 | Russian Doll Envelopes | 2D LIS |
| 35 | Longest String Chain | Subsequence DP |

### ⭐ Must-master

**LIS → Number of LIS → Russian Doll Envelopes**

---

## 🔴 Level 6 — Interval DP

This is where DP starts becoming **significantly harder**.

**Think:**
> "What happens if I split the interval at position `k`?"

| # | Problem | Main Concept |
|---:|---|---|
| 36 | Burst Balloons | Interval DP |
| 37 | Matrix Chain Multiplication | Partition DP |
| 38 | Minimum Cost to Cut a Stick | Interval partition |
| 39 | Palindrome Partitioning | Interval DP |
| 40 | Strange Printer | Interval DP |
| 41 | Optimal BST | Interval DP |

### ⭐ Must-master

**Matrix Chain Multiplication → Burst Balloons → Minimum Cost to Cut a Stick**

---

## 🔴 Level 7 — Advanced DP

These are excellent for **hard interviews**.

| # | Problem | Main Concept |
|---:|---|---|
| 42 | Best Time to Buy and Sell Stock with Cooldown | State-machine DP |
| 43 | Best Time to Buy and Sell Stock III | State-machine DP |
| 44 | Best Time to Buy and Sell Stock IV | K transactions |
| 45 | Regular Expression Matching | String DP |
| 46 | Wildcard Matching | String DP |
| 47 | Minimum Falling Path Sum II | Optimized DP |
| 48 | Profitable Schemes | Multi-dimensional DP |
| 49 | Tallest Billboard | Difference-state DP |

---

## 🟣 Level 8 — Very Hard / Advanced

**Don't start here.** These are useful after you're comfortable with the previous patterns.

| # | Problem | Pattern |
|---:|---|---|
| 50 | Cherry Pickup | 3D DP |
| 51 | Cherry Pickup II | 3D grid DP |
| 52 | Paint House III | Multi-dimensional DP |
| 53 | Scramble String | Interval + string DP |
| 54 | Minimum Difficulty of a Job Schedule | Partition DP |
| 55 | Number of Ways to Wear Different Hats | Bitmask DP |
| 56 | Smallest Sufficient Team | Bitmask DP |
| 57 | Travelling Salesman Problem | Bitmask DP |
| 58 | Digit DP Problems | Digit DP |
| 59 | Tree DP Problems | DP on trees |

---

# 🎯 Recommended Learning Order

Follow the levels in order rather than jumping directly to the hard problems.

```text
Level 1
  ↓
1D DP Fundamentals
  ↓
Level 2
  ↓
Grid DP
  ↓
Level 3
  ↓
Knapsack / Subset DP
  ↓
Level 4
  ↓
String DP
  ↓
Level 5
  ↓
LIS / Subsequence DP
  ↓
Level 6
  ↓
Interval DP
  ↓
Level 7
  ↓
Advanced DP
  ↓
Level 8
  ↓
Very Hard / Advanced DP
```

## 🧠 Core DP Patterns to Master

By the end of this roadmap, you should be comfortable identifying these major patterns:

1. **1D DP**
2. **Take / Not Take**
3. **Grid DP**
4. **Knapsack DP**
5. **Subset DP**
6. **Counting DP**
7. **String DP**
8. **LCS**
9. **LIS**
10. **Interval / Partition DP**
11. **State-machine DP**
12. **Multi-dimensional DP**
13. **Bitmask DP**
14. **Digit DP**
15. **Tree DP**

---

## ⭐ Highest-Priority Problems

If you have limited time, prioritize these:

### Fundamentals
- Climbing Stairs
- House Robber
- Decode Ways

### Grid
- Unique Paths
- Minimum Path Sum
- Dungeon Game

### Knapsack / Subset
- 0/1 Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Coin Change
- Target Sum

### String
- Longest Common Subsequence
- Edit Distance
- Distinct Subsequences
- Word Break

### LIS
- Longest Increasing Subsequence
- Number of LIS
- Russian Doll Envelopes

### Interval
- Matrix Chain Multiplication
- Burst Balloons
- Minimum Cost to Cut a Stick

---

# Tip for Mastering Dynamic Programming

Firstly master **recursion**, all these problems are first solved using recursion and then memoization is applied.

If you know how to write a recursive solution, then DP is just a piece of cake.

For every problem:

```text
Write recursive solution
  ↓
Apply Memoization by recognising states
  ↓
Try to write Tabulation method
  ↓
If okay, try to further optimize space
  (can easily be done in 1D DP)
```

Although this repo contains only **recursive + memoized solutions**, in the future I will upload the same problems using **only the tabulation approach**.
