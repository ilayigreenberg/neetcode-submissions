class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total, amount = 0, 0
        while l < r and r < len(height):

            if height[l] > height[r]:
                amount += height[l] - height[r]
            else:
                total += amount
                amount = 0
                l = r
            r += 1

        return total
