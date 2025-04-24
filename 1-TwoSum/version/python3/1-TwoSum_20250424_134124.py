# Last updated: 4/24/2025, 1:41:24 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]]=i
            elif nums[i] in d:
                return [d[nums[i]],i]
        return [-1,-1]