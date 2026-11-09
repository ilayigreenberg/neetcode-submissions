class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = defaultdict(list)
        for num in nums:
            if num not in buckets[1]:
                buckets[1].append(num)
                continue
            i = 2
            while num in buckets[i]:
                i += 1
            buckets[i].append(num)

        return buckets[k]

