class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import defaultdict

        timeLeft = defaultdict(int)
        fleets = defaultdict(list)
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            timeLeft[position[i]] = time
            fleets[time].append(position[i])

        position.sort()
        for i in range(len(position) - 1):
            if timeLeft[position[i]] <= timeLeft[position[i + 1]]:
                fleets[timeLeft[position[i]]].remove(position[i])
                if not fleets[timeLeft[position[i]]]:
                    del fleets[timeLeft[position[i]]]
       
        return len(fleets)

