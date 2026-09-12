class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # [-4,-1,-1,0,1,2] x + y = -num (1)
        output = []
        for i in range(len(nums)):
            if nums[i] != nums[i-1] or i==0:
                left = i + 1
                right = len(nums) - 1
                while right > left:
                    if nums[right] + nums[left] > -nums[i]:
                        right -=1
                    elif nums[right] + nums[left] < -nums[i]:
                        left+=1
                    else:
                        output.append([nums[left],nums[i],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left]==nums[left-1] :
                            left +=1
                        while left < right and nums[right]==nums[right+1]:
                            right-=1
                        

        return output


                
            
            
            

            



        

        