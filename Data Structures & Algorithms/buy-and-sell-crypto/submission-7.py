class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrf, acc = 0, 0 
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff >= 0:
                acc += diff
            else:
                if acc > maxPrf:
                    maxPrf = acc
                if acc + diff >= 0:
                    acc += diff
                else:
                    acc = 0
        if acc > maxPrf:
            maxPrf = acc
        return maxPrf

"""    1 - 10 = -9
       5 - 1  =  4   |
       6 - 5  =  1   |-  6
       7 - 6  =  1   |
       1 - 7  = -6

       3 - 1  =  2   |
       4 - 3  =  1   |
       5 - 4  =  1   |-  6
       6 - 5  =  1   |
       7 - 6  =  1   |

    [10,1,5,6,7,1, 3..]"""