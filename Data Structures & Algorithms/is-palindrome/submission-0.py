class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""
        for caract in s:
            if caract.isalnum():
                clean += caract.lower()
        
        check = ""
        for i in range(-1,-len(clean)-1,-1):
            check += clean[i]

        return check == clean





        