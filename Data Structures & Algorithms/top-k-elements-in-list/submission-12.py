class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import defaultdict

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1  
        sorted_counter = sorted(counter.items(), key = lambda item : item[1])
        
        res = []
        for i in range(k):
            res.append(sorted_counter.pop()[0])
        return res
