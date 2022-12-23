class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = dict()
        for i in range(len(nums)):
            if target-nums[i] in nummap.keys():
                return nummap[target-nums[i]],i
            else:
                nummap[nums[i]] = i
        return 
