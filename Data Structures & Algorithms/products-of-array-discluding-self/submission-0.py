class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixe = [1]*len(nums)
        for i in range(1,len(nums)):
            prefixe[i] = prefixe[i-1] * nums[i-1]
            

        sufixe = [1]*len(nums)
        for i in range(-2,-len(nums)-1,-1):
            sufixe[i] = sufixe[i+1] * nums[i+1]


        result = [pre * suf for pre,suf in zip(prefixe,sufixe)]
        return result


        


