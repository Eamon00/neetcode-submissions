class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0

        for i in range(len(s)):
            r = i + 1
            checkstring = s[l:r]
            count = {}
            valcount = 0

            for character in checkstring:
                count[character] = 1 + count.get(character, 0)

            for num in count.values():
                valcount += num
            
            if valcount - max(count.values()) <= k:
                res = max(res, r-l)
            else:
                l += 1

        return res


        # max(count.values())
        # max(count)        
        # l,r = 0
        # add 1 to r, check number of unique letters vs k
        # update res
        # if unique > k, add 1 to l

    