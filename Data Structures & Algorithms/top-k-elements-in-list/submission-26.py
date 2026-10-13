class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import defaultdict
        counter = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]   # so freq[len(nums)] won't be an error

        for n in nums:
            counter[n] += 1  # { 1 : 4, 5 : 2, 3 : 1}    1 <= c <= len(nums)
    
        res, j = [], 0
        for n, c in counter.items():
            freq[c].append(n)    # [ [*Nothing*], [3], [5], [], [1], [], [], [] ]
        
        for i in range(len(nums), 0, -1):
            for m in freq[i]:
                res.append(m)
                j += 1
                if j == k:
                    return res
            


     #  nums = [1,5,1,1,3,5,1] , len = 7 , k = 2   res = [1,5]


        

