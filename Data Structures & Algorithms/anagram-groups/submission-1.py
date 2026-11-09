class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        for s in strs:  # O(m)
            angKey = [] * 26
            for c in s:  # O(n)
                angKey[ord(c) - ord('a')] += 1
            res[angKey].append(s)
        return res.values
            