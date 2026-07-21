class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        
        for char in t:
            if char not in dS:
                return False
            
            if dT[char] != dS[char]:
                return False
        
        return True
            

