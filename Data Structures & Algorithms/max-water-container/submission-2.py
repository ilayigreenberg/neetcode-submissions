class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = self.area(l, r, heights)
        while l < r:                
            if heights[l] < heights[r]: 
               #so reducing r only decreases the area
                l += 1
                maxWater = max(maxWater, self.area(l, r, heights))

            else: 
               #so increasing l only decreases the area
                r -= 1    
                maxWater = max(maxWater, self.area(l, r, heights))
        
        return maxWater


    def area(self, l, r, heights):
        return (r - l) * (min(heights[l], heights[r]))