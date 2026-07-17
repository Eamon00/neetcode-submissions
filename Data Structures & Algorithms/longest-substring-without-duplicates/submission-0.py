class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        res = 0

        for i in range(len(s)):
            if s[i] in count:
                l = max(count[s[i]] + 1, l)
            count[s[i]] = i
            res = max(res, i - l + 1)
        return res