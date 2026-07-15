class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        maxseq = 1
        length = len(nums)
        
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        
        if length == 0:
            return 0
        
        for i in nums:
            if (i - 1) not in count:
                maxseqtemp = 0
                for numbers in range(length):
                    if (numbers + i) in count:
                        maxseqtemp += 1
                        maxseq = max(maxseq, maxseqtemp)
                    else:
                        break
            else:
                continue
                
        return(maxseq)