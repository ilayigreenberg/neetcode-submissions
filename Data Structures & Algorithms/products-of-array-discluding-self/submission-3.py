class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * (n - 1), [1] * (n - 1)

        for i in range(1, n - 1):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(n - 1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]

        for i in range(0, n):
            nums[i] = prefix[i] * suffix[i]
        return nums