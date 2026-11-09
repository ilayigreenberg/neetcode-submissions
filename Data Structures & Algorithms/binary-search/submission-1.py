class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = end // 2
            if target < nums[idd]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            elif target == nums[mid]:
                return mid
        return -1
