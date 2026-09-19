class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_frequence={}
        left = 0
        freq_max=0
        max_length = 0


        for right in range(len(s)):
            window_frequence[s[right]] = window_frequence.get(s[right],0)+1
            freq_max=max(freq_max,window_frequence[s[right]])
            if right-left+1 > freq_max+k:
                window_frequence[s[left]]-=1
                left+=1
            max_length = max(right-left+1,max_length)
            

        
        return max_length


                



        