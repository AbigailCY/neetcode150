from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [0] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] *  nums[i-1]
            right[-i-1] = right[-i] * nums[-i]
        for i in range(len(nums)):
            res[i] = left[i]* right[i]
        return res