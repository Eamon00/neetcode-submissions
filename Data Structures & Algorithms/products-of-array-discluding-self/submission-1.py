class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalsum = 1
        zero_cnt = 0
        n = len(nums)
        res = []
    
        for i in nums:
            if i == 0:
                zero_cnt += 1
                continue
            totalsum *= i
    
        if zero_cnt > 1:
            for i in range(n):
                res.append(0)
            return(res)
    
        if zero_cnt == 1:
            for i in range(n):
                if nums[i] == 0:
                    res.append(totalsum)
                else:
                    res.append(0)
            return(res)
        
        if zero_cnt == 0:
            for i in range(n):
                res.append(int(totalsum/nums[i]))
    
            return(res)
           