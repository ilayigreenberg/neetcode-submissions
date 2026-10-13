class Solution:
    def trap(self, height: list[int]) -> int:
        count = 0
        l, r = 0, 1
        while l < len(height):
            l, h = self.check(l, l + 1, height)
            if l == -1 or l >= len(height) - 2:
                return count
            r = l + 1
            while r < len(height) and h > height[r]:
                count += h - height[r]
                r += 1
            l = r
       # return count

    def check(self, l, r, height):
        bottom, maxr = False, 0
        while r < len(height):
            #if we reach the bottom
            if not bottom and height[r] > height[r - 1]: 
                bottom = True
                maxr = r
            if bottom and height[r] > height[maxr]:
                maxr = r
            #if somewhere height[r] gets bigger than/equal to height[l]
            if not height[l] > height[r]:  
                return l, height[l]
            r += 1
        if not bottom:
            return l, 0
        return l, height[maxr]