# LEETCODE 136

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        # XOR all numbers in the array
        for num in nums:
            ans = ans ^ num
            
        return ans
