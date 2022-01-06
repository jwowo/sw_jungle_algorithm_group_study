from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        counter = Counter(stones)
        
        for jewel in jewels:
            total += counter[jewel]
            
        return total