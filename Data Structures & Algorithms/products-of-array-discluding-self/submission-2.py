class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        prefix, suffix = [1] * n , [1] * n

        for i in range(0, n - 1):
            prefix[i + 1] = prefix[i] * nums[i]

        for i in range(n - 1, -1, -1):
            suffix[i - 1] = suffix[i] * nums[i]

        for i in range(0, n):
            nums[i] = prefix[i] * suffix[i]
        return nums