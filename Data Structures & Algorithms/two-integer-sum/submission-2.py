class Solution:
    def twoSum(self, nums, target: int):
        complement = {}
        for i, n in enumerate(nums):
            complement[n] = (target - n, i)
        
        for n, tup in complement.items():
            if tup[0] in complement:
                i, j = tup[1], complement[tup[0]][1]
                return [i, j] if i < j else [j, i]