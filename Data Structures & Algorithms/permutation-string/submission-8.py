class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        validation = {}

        for char in s1:
            validation[char]= validation.get(char,0) + 1

        window = {}
        left = 0
        max_len = len(s1)

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0) + 1
            
            if right-left+1 > max_len:
                window[s2[left]] = window.get(s2[left],0) - 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left+=1
            if window == validation:
                return True
                
            
        return False
            





