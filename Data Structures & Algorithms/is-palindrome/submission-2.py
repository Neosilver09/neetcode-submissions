class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""
        for caract in s:
            if caract.isalnum():
                clean += caract.lower()


        return clean[::-1] == clean





        