class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import deque
        seqs = deque([])

        for n in nums:
            for seq in seqs:
                if n < seq[0]:
                    if seq[0] - n == 1:
                        seq.appendleft(n)
                    else:
                        seqs.appendleft(deque([n]))
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
