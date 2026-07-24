class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        counts2 = {}
        lengths1 = len(s1)
        lengths2 = len(s2)
        

        if lengths2 < lengths1:
            return False
        
        for letter in s1:
            counts1[letter] = 1 + counts1.get(letter, 0)

        for char in s2[:lengths1]:
            counts2[char] = 1 + counts2.get(char, 0)

        l, r = 0, lengths1

        while r < lengths2:
            if counts1 == counts2:
                return True
            
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            l += 1

            counts2[s2[r]] = 1 + counts2.get(s2[r], 0)
            r += 1


        return counts2 == counts1
                
                

            








# initialise a count
# iterate over s2 with window size len(s1). Update count as you traverse
# compare counts of s1 and s2 at each window
#