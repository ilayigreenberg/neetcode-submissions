class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        lst = [-n for n in stones]
        heapq.heapify(lst)

        while len(lst) > 1:

            x = heapq.heappop(lst)
            y = heapq.heappop(lst)
            if x != y:
                heapq.heappush(lst, -abs(x-y))

        return -lst[0] if lst else 0