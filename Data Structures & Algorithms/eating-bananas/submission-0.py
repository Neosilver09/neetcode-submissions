class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles)

        while left<=right:
            mid = (left+right)//2
            time = 0
            for bananes in piles:
                time+=(bananes+mid-1)//mid
            if time<=h:
                if result>=mid:
                    result = mid
                right = mid-1
            else:
                left = mid + 1
        
        return result





        