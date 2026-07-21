class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dS={}
        dT={}
        for char in s:
            if char not in dS:
                dS[char] = 1
            else:
                dS[char]+=1
        
        for char in t:
            if char not in dT:
                dT[char] = 1
            else:
                dT[char]+=1
        
        for char in s:
            if char not in dT:
                return False
            
            if dS[char] != dT[char]:
                return False
        
        return True
            

