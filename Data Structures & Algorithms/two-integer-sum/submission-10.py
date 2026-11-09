class Solution:
    def twoSum(self, nums, target: int):
        complement = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in complement:
                j = complement[comp]
                return [j, i]
            complement[n] = i
        
        