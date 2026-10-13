class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #from collections import defaultdict
        res = defaultdict(list)
        for s in strs:  # O(m)
            angKey = [0] * 26
            for c in s:  # O(n)
                angKey[ord(c) - ord('a')] += 1
            res[tuple(angKey)].append(s)
        return list(res.values())
            