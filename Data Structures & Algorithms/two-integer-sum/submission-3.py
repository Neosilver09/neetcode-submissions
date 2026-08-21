class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {valeur : index for index, valeur in enumerate(nums)}
        for i,valeur in enumerate(nums):
            j = dico.get(target - valeur,"False")
            if j != "False" and i!=j:
                return [i,j]
        return None

        
        

        