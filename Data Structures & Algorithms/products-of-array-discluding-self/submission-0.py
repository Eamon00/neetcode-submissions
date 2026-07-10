class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            list_without_i = []
            sum = 1
            list_without_i = nums.copy()
            list_without_i.pop(i)

            for num in range(len(list_without_i)):
                sum = sum * list_without_i[num]

            res.append(sum)

        return res
