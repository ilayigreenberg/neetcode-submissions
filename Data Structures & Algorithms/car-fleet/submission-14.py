class Solution:
    def carFleet(self, target, position, speed):
        from collections import defaultdict

        timeLeft = defaultdict(int)
        fleets = defaultdict(set)
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            timeLeft[position[i]] = time
            fleets[time].add(position[i])

        position.sort()
        for i in range(len(position) - 1, 0, -1):
            if timeLeft[position[i]] > timeLeft[position[i - 1]]:
                # adding position i-1 to position i's fleet
                fleets[timeLeft[position[i]]].add(position[i - 1])
                # removing position i-1 from his timeLeft fleet
                fleets[timeLeft[position[i - 1]]].remove(position[i - 1])
                if not fleets[timeLeft[position[i - 1]]]:
                    del fleets[timeLeft[position[i - 1]]]
                # updating position i-1 new timeLeft
                timeLeft[position[i - 1]] = timeLeft[position[i]]
       
        return len(fleets)

