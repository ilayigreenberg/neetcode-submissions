class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i, l, r = 0, 1, len(nums) - 1
        a, b, c = None, None, None
        while i < len(nums) - 2:
            if l == r:  # updating i to next potential a
                i += 1
                while a is not None and i < len(nums) - 2 and nums[i] == a:
                    i += 1
                l, r = i + 1, len(nums) - 1
                
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:  l += 1
            elif sum > 0:  r -= 1
            else:
                if c == nums[r] and a == nums[i]:
                    r -= 1
                elif b == nums[l] and a == nums[i]:
                    l += 1                                                            
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    a, b, c = nums[i], nums[l], nums[r]

        return res
