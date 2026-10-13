class Solution:
    def topKFrequent(self, nums, k: int):
        counter = [set() for i in range(len(nums))]
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
                counter[0].add(n)
                continue

            for i in range(len(nums)):
                if n not in counter[i]:
                    continue
                counter[i+1].add(n)
                counter[i].remove(n)
                break
        
        while not counter[-1]:
            counter.pop()
        res = []
        for i in range(k):
            while not counter[-1]:
                counter.pop()
            res.append(counter[-1].pop())

        return res

        """
        nums = [1,2,2,3,3,3]  len = 6
        counter = [ [1], [2], [3], [], [], [] ]  k = 2

        nums = [1,1,1,2,2,3]  len = 6
        counter = [ [3], [2], [1], [], [], [] ]  k = 2"""