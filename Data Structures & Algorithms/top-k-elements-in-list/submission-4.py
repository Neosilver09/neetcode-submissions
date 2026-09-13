from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = defaultdict(int)
        for number in nums :
            dico[number] +=1
        output = sorted(dico, key = lambda key: dico[key])
        return output[-k:]

