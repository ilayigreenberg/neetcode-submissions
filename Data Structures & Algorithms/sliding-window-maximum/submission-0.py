class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        window = [-nums[i] for i in range(k)]   #O(k) space
        heapq.heapify(window)   #O(k) time
        deleted = set()
        res = [0] * (len(nums) - k + 1)

        Max = window[0]
        res[0] = Max
        l, r = 0, k

        while r < len(nums):

            heapq.heappush(window, -nums[r]) # insert the r's num into window
            deleted.add(nums[l])
            while window[0] in deleted:
                heapq.heappop(window)
            Max = max(Max, window[0])
            l, r = l+1, r+1
            res[l] = Max
        
        return res

  