class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l, r = 0, 0
        if not s: return 0
        count = defaultdict(int, {s[0]: 1})  # monitor each char occurrence in our window
        common = s[0]   # most frequent char in our window
        chars = 1   # total chars in our window
        longest = 1


        while r < len(s):

            if chars - count[common] < k:           
                count[s[r]] += 1
                if count[s[r]] > count[common]:
                    common = count[s[r]]
                r += 1
                chars += 1
                continue
            
            longest = max(longest, r - l)
            count[s[l]] -= 1
            if s[l] == common:
                common = max(count.values())
            l += 1
            chars -= 1

        longest = max(longest, r - l)
        return longest







            

