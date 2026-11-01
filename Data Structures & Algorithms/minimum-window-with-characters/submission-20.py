class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        chars, seen, extra = defaultdict(int), defaultdict(int), defaultdict(int)
        for c in t:
            seen[c] += 1
            chars[c] += 1

        shortest = ''
        l, r = 0, 0

        while True:

            if r == len(s) and seen:    break
            # as long as we didn't pass all chars, only moving right can help us
            if seen:
                if s[r] in seen:
                    seen[s[r]] -= 1
                    if seen[s[r]] == 0:   del seen[s[r]]
                elif s[r] in chars:
                    extra[s[r]] += 1
                r += 1

            else:   # checking if shorter and keep shorten
                if not shortest or (r - l) < len(shortest):
                    shortest = s[l:r]
                if s[l] in chars:
                    if s[l] in extra:
                        extra[s[l]] -= 1
                        if extra[s[l]] == 0:   del extra[s[l]]
                    else:
                        seen[s[l]] += 1
                l += 1

        return shortest