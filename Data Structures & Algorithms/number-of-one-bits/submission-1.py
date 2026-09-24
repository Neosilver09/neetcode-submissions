class Solution:
    def hammingWeight(self, n: int) -> int:

        quotient,reste = divmod(n,2)
        uns = 1 if reste==1 else 0

        while quotient:
            quotient,reste= divmod(quotient,2)
            if reste == 1 :
                uns+=1
        
        return uns
        