class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        for coords in points:
            coords = (sqrt(coords[0]**2 + coords[1]**2), coords)

        heapq.heapify(points)   # O(n) time
        res = []
        for i in range(k):  # O(k) time
            
            res.append(heapq.heappop(points)[1])  # O(k) space
        
        return res