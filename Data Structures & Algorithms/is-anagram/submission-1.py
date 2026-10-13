class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        encounter = defaultdict(int)
        if len(s) != len(t): 
            return False
        for i in range(len(s)):
            encounter[s[i]] += 1
            encounter[t[i]] -= 1
        for c in encounter:
            if encounter[c] != 0:
                return False
        return True