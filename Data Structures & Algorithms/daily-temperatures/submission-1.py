class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        left = 0
        stack = deque()


        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append(i)

            elif stack and temperatures[stack[-1]]<temp:

                while stack and temperatures[stack[-1]]<temp:
                    
                    last_i = stack.pop()

                    result[last_i]= i-last_i
                stack.append(i)
            else:

                stack.append(i)
            
        return result
                







        