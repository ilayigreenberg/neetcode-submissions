class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total = 0
        bigleft = 0
        while l < r < len(height):

            if height[l] > height[r]:
                r += 1
            else:
                sum = min(height[l], height[r]) - height[l + 1]
                if sum > 0:    total += sum
                l += 1
                