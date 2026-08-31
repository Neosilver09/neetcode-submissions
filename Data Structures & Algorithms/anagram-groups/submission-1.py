class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs : 
            sortedV = sorted(str)
            key = tuple(sortedV)

            if key not in dict : 
                dict[key] = []
            
            dict[key].append(str)

        
        res = []
        for i in dict.values() : 
            res.append(i)
        

        return res

            
            
