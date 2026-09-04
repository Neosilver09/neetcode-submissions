class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)

        output = []

        for i in range(len(numsSorted)):
            if i == 0 or numsSorted[i] != numsSorted[i-1]:
                left = i + 1
                right = len(numsSorted) - 1
                while left < right:
                    if numsSorted[left] + numsSorted[right] < -numsSorted[i]:
                        left += 1
                    elif numsSorted[left] + numsSorted[right] > -numsSorted[i]:
                        right -=1
                    else:
                        output.append([numsSorted[left],numsSorted[i],numsSorted[right]])
                        left+=1
                        right-=1
                        while left < right and numsSorted[left] == numsSorted[left - 1]:
                            left += 1
                        while left < right and numsSorted[right] == numsSorted[right + 1]:
                            right -= 1
                    
        return output
                    
                
        
            

        