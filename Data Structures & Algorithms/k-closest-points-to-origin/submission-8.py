class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        distances = [(sqrt(x*x + y*y), [x, y]) for x, y in points]  # O(n) space+time

        heapq.heapify(distances)
        res = []
        for i in range(k):
            
            res.append(heapq.heappop(distances)[1])
        
        return res

