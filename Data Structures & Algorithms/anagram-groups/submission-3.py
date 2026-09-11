class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dico = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            dico[sortedWord].append(word)
        
        return [group for group in dico.values()]
    

            
        