class Solution:
    def twoSum(self, nums, target: int):
        complement = {}
        seen = set()
        for i, n in enumerate(nums):
            comp = target - n
            if comp in complement:
                j = complement[comp][1]
                return [i, j] if i < j else [j, i]
            complement[n] = (comp, i)
        
        