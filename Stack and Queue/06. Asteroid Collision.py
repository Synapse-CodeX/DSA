# LEETCODE 735

from typing import List


class Solution:

    def asteroidCollision(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []

        for i in range(0, n):
            if nums[i] > 0:
                st.append(nums[i])
            else:
                while (
                    len(st) != 0
                    and st[-1] > 0
                    and st[-1] < abs(nums[i])
                ):
                    st.pop()

                if len(st) != 0 and st[-1] == abs(nums[i]):
                    st.pop()
                elif len(st) == 0 or st[-1] < 0:
                    st.append(nums[i])

        return st