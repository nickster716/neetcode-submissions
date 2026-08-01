class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        simplifiedS = ""
        for c in s:
            if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >=97 and ord(c)<=122):
                simplifiedS +=c
            
        i=0
        j=len(simplifiedS)-1
        while i<j:
            if simplifiedS[i] != simplifiedS[j]:
                return False
            i+=1
            j-=1
        
        return True