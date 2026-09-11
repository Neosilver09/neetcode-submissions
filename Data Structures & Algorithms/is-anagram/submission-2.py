class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) :
            return False


        count = {}
        for caract in s:
            count[caract]=count.get(caract,0) + 1

        for caract in t:
            caractCount = count.get(caract,"False")
            if caractCount != "False":
                count[caract] -= 1
        
        for caractCount in count.values():
            if caractCount != 0:
                return False

        return True
            
        
            
            
        