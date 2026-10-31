class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest, seen = 0, set()
        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                biggest = max(biggest, r - l)   # if r hadn't been increased it would have had to be r - l + 1
                seen.remove(s[l])
                l += 1

        biggest = max(biggest, r - l)
        return biggest