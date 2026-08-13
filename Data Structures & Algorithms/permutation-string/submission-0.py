class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # tc O(26n) = O(n)
        # sc O(1) cuz both dict are always 26 char long
        if len(s2) < len(s1):
            return False

        freqMapS1 = {}
        self.formEmptyCharMap(freqMapS1, s1)
        
        for char in s1:
            freqMapS1[char] += 1
        
        freqMapS2 = {}
        self.formEmptyCharMap(freqMapS2, s2)

        i=0
        j= len(s1) - 1
        for x in range(i, j+1):
            freqMapS2[s2[x]] +=1

        while j<len(s2):
            if self.checkIfSameString(freqMapS1, freqMapS2):
                return True
            
            startChar = s2[i]
            freqMapS2[startChar] -= 1
            i+=1

            j+=1
            if j == len(s2):
                return False
            endChar = s2[j]
            freqMapS2[endChar] += 1
        
        return False
        
    
    def checkIfSameString(self, obj1, obj2):
        return list(obj1.values()) == list(obj2.values())
    
    def formEmptyCharMap(self, obj, s):
        for asciC in range(ord('a'), ord('z')+1, 1):
            letter = chr(asciC)
            obj[letter] = 0

