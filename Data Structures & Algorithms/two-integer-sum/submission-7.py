class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dico = {num:index for index,num in enumerate(nums)}
        # {3:0,4:1 ...}

        for i,num in enumerate(nums):
            j = dico.get(target-num) 
            if j and i!=j:
                return [i,j]