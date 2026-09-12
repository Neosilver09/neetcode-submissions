class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dico = {}
        left = 0
        length = 0

        for right,char in enumerate(s):
            if char not in dico:
                dico[char] = right
            elif dico.get(char) >= left:
                left = dico.get(char) + 1
                dico[char]=right
            else:
                dico[char] = right
            
            length = right-left + 1 if right-left + 1 > length else length
        
        return length
            

        