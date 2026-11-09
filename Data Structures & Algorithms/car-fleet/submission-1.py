class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import defaultdict

        dic = defaultdict()
        for i in range(len(position)):
            timeLeft = (target - position[i]) / speed[i]
            dic[timeLeft] += 1
        return len(dic)