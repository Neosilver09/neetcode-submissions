class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs :
            sort = "".join(sorted(word))
            if dict.get(sort) is None :
                dict[sort] = [word]
            else :
                anags = dict.get(sort)
                anags.append(word)
                dict[sort] = anags
        
        return [anags for anags in dict.values()]

            
                


        