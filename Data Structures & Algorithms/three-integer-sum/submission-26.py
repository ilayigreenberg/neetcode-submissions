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
        complement = set()
        for n in enumerate(nums):
            comp = target - n
            if comp in complement:
                return [comp, n]
            complement.add(n)


            
        complement = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in complement:
                j = complement[comp]
                return [j, i]
            complement[n] = i
        """