class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import deque
        if not nums:
            return 0
            
        seqs = deque([deque([nums[0]])])

        for n in nums:
            i = 0
            while i < len(seqs):
                if n < seqs[i][0]:
                    if seqs[i][0] - n == 1:
                        seqs[i].appendleft(n)
                    else:
                        seqs.append(deque([n]))
                i += 1
        last, lstln = None, None
        maxSeq = 0
        for seq in seqs:
            if seq[0] - 1 == last:
                lstln += len(seq)
            else:
                lstln = len(seq)
            maxSeq = max(maxSeq, len(seq) + lstln)
            last = seq[-1]
        
        return maxSeq
