class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # tc O(n)
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
        
        matches = 0
        for asciiCode in range(ord('a'), ord('z')+1):
            letter = chr(asciiCode)
            if freqMapS1[letter] == freqMapS2[letter]:
                matches+=1
        
        if matches == 26:
            return True
        
        while j<len(s2):
            
            startChar = s2[i]
            wasFreqEqual = freqMapS1[startChar] == freqMapS2[startChar]
            freqMapS2[startChar] -= 1

            if wasFreqEqual:
                matches -= 1
            
            if not wasFreqEqual and freqMapS1[startChar] == freqMapS2[startChar]:
                matches+=1
            i+=1

            j+=1
            if j == len(s2):
                return False
            endChar = s2[j]
            wasEndCharFreqEqual = freqMapS1[endChar] == freqMapS2[endChar]

            freqMapS2[endChar] += 1
            if freqMapS1[endChar] == freqMapS2[endChar]:
                matches += 1
            
            if wasEndCharFreqEqual:
                matches -= 1
            
            if matches == 26:
                return True
        
        return False
        
    
    def formEmptyCharMap(self, obj, s):
        for asciC in range(ord('a'), ord('z')+1, 1):
            letter = chr(asciC)
            obj[letter] = 0