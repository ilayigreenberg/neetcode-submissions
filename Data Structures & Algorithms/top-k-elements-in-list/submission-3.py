class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import defaultdict
        n = len(nums)
        buckets = defaultdict(list)
        buckets_size = 0
        for num in nums:
            if num not in buckets[1]:
                buckets[1].append(num)
                if not buckets_size:
                    buckets_size = 1
                continue
            i = 2
            while num in buckets[i]:
                i += 1
            buckets[i].append(num)
            buckets_size = max(buckets_size, i)

        res = []
        j = 0
        for i in range(k):
            if buckets[buckets_size - j]:
                res.append(buckets[buckets_size - j].pop())
            else:
                j += 1
        
        return res


