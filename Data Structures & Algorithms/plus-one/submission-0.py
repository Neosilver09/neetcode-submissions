class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number_str = ""
        res = []
        for i in digits:
            number_str += str(i)
        
        number = int(number_str)
        number +=1
        number_str = str(number)
        for i in number_str:
            res.append(int(i))
        
        return res

        