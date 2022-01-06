from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda item:item[1], reverse=True)        
        
        result = []
        
        for i in range(k):
            result.append(counter[i][0])
            
        return result