class Solution:
    def isPalindrome(self, s: str) -> bool:
        # doesnt use separate string for comparison thats it
        s= s.lower()
        i=0
        j=len(s)-1
        while i<j:
            if self.isValid(s[i]):
                if self.isValid(s[j]):
                    if s[i]!=s[j]:
                        return False
                    i+=1
                    j-=1
                else:
                    j-=1

            
            elif self.isValid(s[j]):
                i+=1
            
            else:
                i+=1
                j-=1

        return True
            
    def isValid(self, character):
        return (ord(character) >=48 and ord(character) <=57) or (ord(character) >=97 and ord(character) <= 122)