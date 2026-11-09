class Solution:
    def threeSum(self, nums):
        def twoSum(nums, target: int):
            if target in seen:  return

            complement = {}
            for i, n in enumerate(nums):
                if n in seen:  continue  # not necessary

                comp = target - n
                if comp in complement:
                    j = complement[comp]
                    return [j, i]
                complement[n] = i


        seen = set()
        result = []
        for n in nums:
            solution = twoSum(nums, n)
            if not solution:   continue
            else:
                result.append([nums[i] for i in solution] + [n])
        
        return result