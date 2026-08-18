 # 1. Brute Force Recursion

def climbStairs(n):
# Base cases: if n is 0 or 1, there is only 1 way
if n <= 1:
return 1
return climbStairs(n - 1) + climbStairs(n - 2)


# 2. Memoization (Top-Down)
# This stores results in a list to avoid redundant calculations (time and space).

def climbStairs(n, memo={}):
if n in memo: return memo[n]
if n <= 1: return 1
memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
return memo[n]

# 3. Tabulation (Bottom-Up)
# This builds the solution iteratively from up to (time and space).


def climbStairs(n):
if n <= 1: return 1
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
dp[i] = dp[i-1] + dp[i-2]
return dp[n]

# 4. Space-Optimized Tabulation
# This reduces space to by keeping only the last two values.


def climbStairs(n):
if n <= 1: return 1
prev2, prev1 = 1, 1
for i in range(2, n + 1):
curr = prev1 + prev2
prev2 = prev1
prev1 = curr
return prev1
