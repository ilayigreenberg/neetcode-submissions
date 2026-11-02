class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict
        window = [-nums[i] for i in range(k)]   #O(k) space
        heapq.heapify(window)   #O(k) time
        deleted = defaultdict(int)
        res = [0] * (len(nums) - k + 1)

        Min = window[0]
        res[0] = -Min
        l, r = 0, k

        while r < len(nums):

            heapq.heappush(window, -nums[r]) # insert the r's num into window
            deleted[-nums[l]] += 1
            while window and window[0] in deleted:
                deleted[window[0]] -= 1
                if deleted[window[0]] == 0:    del deleted[window[0]]
                heapq.heappop(window)
            Min = window[0]
            l, r = l+1, r+1
            res[l] = -Min

        return res