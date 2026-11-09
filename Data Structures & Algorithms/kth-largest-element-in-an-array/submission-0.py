class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)
            
        return heapq.heappop(nums)