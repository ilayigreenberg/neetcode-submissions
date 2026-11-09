class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for n in nums:
            complement[n] = target - n
        
        for n1, n2 in complement.items():
            if n2 in complement:
                return [n1, n2]