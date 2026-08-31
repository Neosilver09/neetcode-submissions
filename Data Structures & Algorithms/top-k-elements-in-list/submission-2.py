class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums :
           
            count[num] = 1 + count.get(num,0)


        heap = []
        for num, i in count.items() :
            heapq.heappush(heap,(i, num))

            if len(heap) > k : 
                heapq.heappop(heap)

        res = [valeur for cle,valeur in heap]
      

        return res


            

         

