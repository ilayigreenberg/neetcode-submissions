class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        triplets = set()

        for targetIndex, target in enumerate(nums):

            complement = set()
            for i, n in enumerate(nums):
                if i == targetIndex:
                    continue
                comp = -target - n
                if comp in complement:
                    triplet = tuple(sorted([target, comp, n]))
                    if triplet not in triplets:
                        triplets.add(triplet)
                        res.append(list(triplet))
                complement.add(n)
                
        return res




        """
        comp = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in comp:
                j = comp[c]
                return [j, i]
            comp[n] = i
        """