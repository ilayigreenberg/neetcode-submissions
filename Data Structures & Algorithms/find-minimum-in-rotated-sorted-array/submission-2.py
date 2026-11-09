class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                start = mid - 1
            elif nums[start] > nums[mid]:
                end = mid
            elif nums[start] == nums[mid]:
                return nums[mid + 1]