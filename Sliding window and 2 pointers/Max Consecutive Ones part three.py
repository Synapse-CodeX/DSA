# LEETCODE 1004

# 1. Brute Force Approach (O(N²))
 

def longestOnes_brute(nums, k):
    n = len(nums)
    maxi = 0
    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                break
            maxi = max(maxi, j - i + 1)
    return maxi


# 2. Better Sliding Window Approach (O(2N))


def longestOnes_better(nums, k):
    left = 0
    maxi = 0
    zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        maxi = max(maxi, right - left + 1)
    return maxi


# 3. Optimal Sliding Window Approach (O(N))


def longestOnes_optimal(nums, k):
    left = 0
    maxi = 0
    zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        maxi = max(maxi, right - left + 1)
    return maxi
