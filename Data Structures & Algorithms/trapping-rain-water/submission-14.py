class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total = 0
        while l < r < len(height):

            if height[l] > height[r]:
                r += 1
            else:
                total += min(height[l], height[r]) - height[l + 1]
                l += 1
                