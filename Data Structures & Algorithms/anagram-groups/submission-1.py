class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            the_list = hashy.get(sorted_word, [])
            the_list.append(word)
            hashy[sorted_word] = the_list
    
        res = []
        for x, y in hashy.items():
            res.append(y)
        
        return(res)