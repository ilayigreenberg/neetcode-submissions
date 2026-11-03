class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x*x + y*y, [x, y]) for x, y in points]  # O(n) space+time

        heapq.heapify(distances)
        res = []
        for i in range(k):
            
            res.append(heapq.heappop(distances)[1])
        
        return res

