class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dico = {num:index for index,num in enumerate(nums)}

        for i,num in enumerate(nums):
            j = dico.get(target-num,"False")
            if j != "False" and i!=j:
                return [i,j]