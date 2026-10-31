class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)  # monitor each char occurrence in our window
        common = []  # most frequent char(s) in our window
        longest = 0
        l, r = 0, 0  # total chars in our window = (r - l)

        while r < len(s):

            if s[r] in common or not common:
                common.clear()
                common.append(s[r]) # cause now it's the only most frequent char in our chars
                count[s[r]] += 1
                r += 1

            elif (r - l) - count[common[0]] < k:
                if count[s[r]] + 1 == count[common[0]]:
                    common.append(s[r])
                count[s[r]] += 1
                r += 1

            else:
                longest = max(longest, r - l)
                count[s[l]] -= 1
                MaxFreq = max(count.values())
                common = [c for c, n in count.items() if n == MaxFreq != 0]
                l += 1

        longest = max(longest, r - l)
        return longest