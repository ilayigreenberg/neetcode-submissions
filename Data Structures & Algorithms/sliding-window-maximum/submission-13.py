class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        window = [-nums[i] for i in range(k)]   #O(k) space
        heapq.heapify(window)   #O(k) time
        deleted = defaultdict(int)
        res = [0] * (len(nums) - k + 1)

        res[0] = -window[0]
        l, r = 0, k

        while r < len(nums):

            heapq.heappush(window, -nums[r]) # insert the r's num into window
            if -nums[l] not in deleted:
                deleted[-nums[l]] = 1
            if window and window[0] in deleted:
                deleted[window[0]] -= 1
                if deleted[window[0]] == 0:    del deleted[window[0]]
                heapq.heappop(window)
            l, r = l+1, r+1
            res[l] = -window[0]

        return res