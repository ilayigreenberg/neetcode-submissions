class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        for i in range(len(points)):
            points[i] = (sqrt(points[i][0] ** 2 + points[i][1] ** 2), points[i])

        heapq.heapify(points)   # O(n) time
        res = []
        for i in range(k):  # O(k) time
            
            res.append(heapq.heappop(points)[1])  # O(k) space
        
        return res