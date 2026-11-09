class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        window = [-nums[i] for i in range(k)]   #O(k) space
        heapq.heapify(window)   #O(k) time
        deleted = set()
        res = [0] * (len(nums) - k + 1)

        Min = window[0]
        res[0] = -Min
        l, r = 0, k

        while r < len(nums):

            heapq.heappush(window, -nums[r]) # insert the r's num into window
            deleted.add(-nums[l])
            while window and window[0] in deleted:
                heapq.heappop(window)
            Min = min(Min, window[0]) if window else Min
            l, r = l+1, r+1
            res[l] = -Min

        return res