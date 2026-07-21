class Solution:
    # without space
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        