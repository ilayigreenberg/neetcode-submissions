class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxseq = 0 
        for n in nums:
            if n - 1 not in numset:
                count = 1
                while n + count in numset:
                    count += 1
                maxseq = max(maxseq, count)
        return maxseq      
                