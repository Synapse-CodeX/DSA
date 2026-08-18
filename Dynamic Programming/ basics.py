# FIBONACCI USING DP


# 1. Normal Recursion
def fib(num):
    if num == 0: return 0
    if num == 1: return 1
    return fib(num - 1) + fib(num - 2)

# 2. Memoization
def fib_memo(num, dp):
    if num <= 1: return num
    if dp[num] != -1: return dp[num]
    dp[num] = fibmemo(num - 1, dp) + fibmemo(num - 2, dp)
    return dp[num]

# 3. Tabulation
def fib_tabulation(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 4. Tabulation with Space Optimization
def fibspaceoptimized(n):
    prev2 = 0
    prev = 1
    for i in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev
