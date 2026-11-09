class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        chars, seen = defaultdict(int), defaultdict(int)
        for c in t:
            seen[c] += 1
            chars[c] += 1

        shortest = ''
        l, r = 0, 0

        while r <= len(s):

            if seen and r < len(s):    # as long as we didn't pass all chars, only moving right can help us
                if s[r] in chars:
                    seen[s[r]] -= 1         #
                    if seen[s[r]] == 0:     # - all same action
                        del seen[s[r]]      #
                r += 1

            if not seen:   # checking if shorter and keep shorten
                if not shortest or (r - l) < len(shortest):
                    shortest = s[l:r]
                if s[l] in chars:
                    seen[s[l]] += 1
                l += 1

        return shortest
