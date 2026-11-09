class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        chars, seen = defaultdict(int), defaultdict(int)
        for c in t:
            seen[c] += 1
            chars[c] += 1

        shortest = ''
        l, r = 0, 0

        while True:          
            if r == len(s) and any(v > 0 for v in seen.values()):
                break
            # as long as we didn't pass all chars, only moving right can help us
            if any(v > 0 for v in seen.values()):
                if s[r] in chars:
                    seen[s[r]] -= 1
                r += 1

            else:   # checking if shorter and keep shorten
                if not shortest or (r - l) < len(shortest):
                    shortest = s[l:r]
                if s[l] in chars:
                    seen[s[l]] += 1
                l += 1

        return shortest