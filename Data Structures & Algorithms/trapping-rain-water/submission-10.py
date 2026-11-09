class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total, amount = 0, 0
        while l < r:

            if height[l] > height[r]:
                amount += height[l] - height[r]
            else:
                total += amount
                l = r
            r += 1

        return total
