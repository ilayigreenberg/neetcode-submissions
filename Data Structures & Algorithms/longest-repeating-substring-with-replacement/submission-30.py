class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)  # monitor each char occurrence in our window
        common = ''  # most frequent char(s) in our window
        longest = 0
        l, r = 0, 0  # total chars in our window = (r - l)

        while r < len(s):

            if count[s[r]] == count[common] or not common:
                common = s[r] # cause now it's the only most frequent char in our chars
                count[s[r]] += 1
                r += 1

            elif (r - l) - count[common] < k:
                #if count[s[r]] + 1 == count[common]:
                #    common = s[r]
                count[s[r]] += 1
                r += 1

            else:
                longest = max(longest, r - l)
                count[s[l]] -= 1
                common = max(count, key= count.get)
                l += 1

        longest = max(longest, r - l)
        return longest
