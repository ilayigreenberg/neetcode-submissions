class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        for n in nums:
            res = twoSum(nums, n)
            if not res:   continue
            else:
                return [nums[i] for i in res] + [n]


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