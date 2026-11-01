class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        seen = defaultdict(int)
        for c in s1:
            seen[c] += 1
        l, r = 0, 0
        
        while r < len(s2):

            if s2[r] in seen:
                seen[s2[r]] -= 1
                if seen[s2[r]] == 0:  del seen[s2[r]]
                r += 1

            elif l < r:
                seen[s2[l]] += 1
                l += 1

            else:   # implies that both l and r at char that doesn't exist in s1
                l = r = r + 1    # (and we've already updated seen back in l's way right

            if not seen:
                return True
        
        return False