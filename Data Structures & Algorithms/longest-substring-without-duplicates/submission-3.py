class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        longestS = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left+=1
            
            charSet.add(s[r])
            longestS = max(longestS, r-left+1)
        
        return longestS