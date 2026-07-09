class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
    
        listcount = []
        for num, freq in count.items():
            listcount.append([freq, num])
        listcount.sort()
    
        result = []
        while len(result) < k:
            result.append(listcount.pop()[1])
        return(result)        