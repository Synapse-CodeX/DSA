# LEETCODE 2220

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Step 1: Find the positions where bits differ using XOR
        xor_result = start ^ goal
        
        # Step 2: Count the number of set bits (1s)
        count = 0
        while xor_result > 0:
            # Check if the last bit is 1
            count += xor_result & 1
            # Shift right to check the next bit
            xor_result >>= 1
            
        return count
