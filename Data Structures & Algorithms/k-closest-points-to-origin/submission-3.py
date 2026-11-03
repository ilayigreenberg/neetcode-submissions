class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        distances = [(sqrt(coords[0]**2 + coords[1]**2), coords) for coords in points]

        heapq.heapify(distances)
        res = []
        for i in range(k):
            
            res.append(heapq.heappop(distances)[1])
        
        return res

