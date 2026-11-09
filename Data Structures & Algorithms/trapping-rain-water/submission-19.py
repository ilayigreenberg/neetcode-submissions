class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        total = 0
        while r < len(height):
            
            if height[l] > height[r]:
                r += 1
            else: 
                minheight = min(height[l], height[r])
                while l < r:
                    sum = minheight - height[l + 1]
                    if sum > 0:    total += sum
                    l += 1
                r += 1
        
        return total