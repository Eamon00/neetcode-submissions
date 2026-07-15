class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxwater = 0

        while l < r:
            h = min(heights[l], heights[r])
            tempmax =  h * (r-l)
            maxwater = max(maxwater, tempmax)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                
        return(maxwater)