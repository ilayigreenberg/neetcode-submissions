class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]

        for i in range(0, n):
            nums[i] = prefix[i] * suffix[i]
        return nums