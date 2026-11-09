class Solution:
    def longestConsecutive(self, nums) -> int:
        from collections import deque
        if not nums:
            return 0      
        seqs = deque([])

        for n in nums:
            i = 0
            while i < len(seqs):
                if n < seqs[i][0]:
                    if seqs[i][0] - n == 1:
                        seqs[i].appendleft(n)
                        break
                    elif seqs[i][0] != n:
                        seqs.insert(i, deque([n]))
                        break
                    else: 
                        break
                i += 1
            else:
                seqs.append(deque([n]))

        last, lstln = None, None
        maxSeq = 0
        for seq in seqs:
            if seq[0] - 1 == last:
                lstln += len(seq)
            elif seq[0] == last:
                lstln += len(seq) - 1
            else:
                lstln = len(seq)
            maxSeq = max(maxSeq, lstln)
            last = seq[-1]
        
        return maxSeq