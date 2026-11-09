class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        chars, seen = defaultdict(int), defaultdict(int)
        for c in t:
            seen[c] += 1
            chars[c] += 1

        shortest = ''
        l, r = 0, 0

        while r < len(s) + 1:          
            if r == len(s) and seen:   break
            # as long as we didn't pass all chars, only moving right can help us
            if all(v < 1 for v in seen.values()):  # zeros the values doesn't enough - we want to take into account the number of appearances of chars belongs to t so we will know if we can still truncate from left although we at a char belongs to t
                seen[s[r]] -= 1
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