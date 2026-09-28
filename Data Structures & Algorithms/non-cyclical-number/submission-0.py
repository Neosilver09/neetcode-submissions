class Solution:

    def sum_digits(self,n):
        somme = 0
        for i in str(n):
            somme+= int(i)**2
        return somme

    def isHappy(self, n: int) -> bool:

        seen = set()
        while n!=1:
            if self.sum_digits(n) not in seen:
                n = self.sum_digits(n)
                seen.add(n)
            else:
               return False
        
        return True


        
        

