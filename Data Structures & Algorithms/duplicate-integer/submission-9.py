class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for a in (i+1, len(nums)-1):
                if nums[i] == nums[a]:
                    return True

        return False