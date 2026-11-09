class Solution:
    def twoSum(self, nums, target: int):
        complement = {}
        for i, num in enumerate(nums):
            if num not in complement:
                complement[num] = [target - num, i]
            else:
                complement[num].append(i)
        
        for num, comp in complement.items():
            if comp[0] in complement:
                if len(complement[comp[0]]) > 2:
                    i, j = complement[comp[0]][1], complement[comp[0]][2]
                elif num != comp[0]:
                    i, j = comp[1], complement[comp[0]][1]
                else: continue
                return [i, j] if i < j else [j, i]