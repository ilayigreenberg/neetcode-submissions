class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        numsNeg = [-num for num in nums]
        heapq.heapify(numsNeg)

        for i in range(k - 1):
            heapq.heappop(numsNeg)

        return -heapq.heappop(numsNeg)