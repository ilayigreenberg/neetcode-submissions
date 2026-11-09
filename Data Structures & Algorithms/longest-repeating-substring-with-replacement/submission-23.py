class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l, r = 0, 0
        if not s: return 0
        count = defaultdict(int)  # monitor each char occurrence in our window
        common = []  # most frequent char in our window
        chars = 0  # total chars in our window
        longest = 0
        needSort = False

        while r < len(s):

            if s[r] in common or not common:
                common.clear()
                common.append(s[r]) # cause now it's the only most frequent char in our chars
                count[s[r]] += 1
                chars += 1
                r += 1

            elif chars - count[common[0]] < k:
                if count[s[r]] + 1 == count[common[0]]:
                    common.append(s[r])
                count[s[r]] += 1
                chars += 1
                r += 1

            else:
                longest = max(longest, chars)
                count[s[l]] -= 1          #
                #if count[s[l]] == 0:      # same action of updating count
                #    common.remove(s[l])   #
                MaxFreq = max(count, key= count.get)
                common = [c for c, n in count.items() if n == MaxFreq != 0]
                chars -= 1
                l += 1

        longest = max(longest, chars)
        return longest