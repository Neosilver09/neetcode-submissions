class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # On initialise le min-heap avec les K premiers éléments
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # On parcourt le reste des éléments
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        return min_heap[0]
