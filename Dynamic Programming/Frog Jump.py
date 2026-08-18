# 1. Brute Force Recursion

def solve(index, heights):
if index == 0: return 0
# Jump 1
one_jump = solve(index - 1, heights) + abs(heights[index] - heights[index - 1])
# Jump 2
two_jump = float('inf')
if index > 1:
two_jump = solve(index - 2, heights) + abs(heights[index] - heights[index - 2])
return min(one_jump, two_jump)

# 2. Memoization (Top-Down DP)

def solve(index, heights, dp):
if index == 0: return 0
if dp[index] != -1: return dp[index]
one_jump = solve(index - 1, heights, dp) + abs(heights[index] - heights[index - 1])
two_jump = float('inf')
if index > 1:
two_jump = solve(index - 2, heights, dp) + abs(heights[index] - heights[index - 2])
dp[index] = min(one_jump, two_jump)
return dp[index]

# 3. Tabulation (Bottom-Up DP)

def frog_jump(heights):
n = len(heights)
dp = [-1] * n
dp[0] = 0
for i in range(1, n):
jump1 = dp[i-1] + abs(heights[i] - heights[i-1])
jump2 = float('inf')
if i > 1:
jump2 = dp[i-2] + abs(heights[i] - heights[i-2])
dp[i] = min(jump1, jump2)
return dp[n-1]

# 4. Space-Optimized Tabulation

def frog_jump_optimized(heights):
prev = 0
prev2 = 0
for i in range(1, len(heights)):
jump1 = prev + abs(heights[i] - heights[i-1])
jump2 = float('inf')
if i > 1:
jump2 = prev2 + abs(heights[i] - heights[i-2])
current = min(jump1, jump2)
prev2 = prev
prev = current
return prev
