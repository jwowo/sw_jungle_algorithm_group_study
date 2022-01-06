class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = {}
        
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in result and start <= result[char]:
                start = result[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            result[char] = i
            
        return max_length