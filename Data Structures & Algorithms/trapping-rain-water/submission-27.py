class Solution:
    def trap(self, height) -> int:
        l, r = 0, 1
        total, maxright = 0, 0
        while r < len(height):
            if r == len(height):
                while l < r:
                    sum = maxright - height[l + 1]
                    if sum > 0:    total += sum
                    l += 1
            if height[l] > height[r] and r < len(height) - 1:
                r += 1
                maxright = max(maxright, height[r])
            else:
                minheight = min(height[l], height[r])
                while l < r:
                    sum = minheight - height[l + 1]
                    if sum > 0:    total += sum
                    l += 1
                maxright = 0
                r += 1

        return total