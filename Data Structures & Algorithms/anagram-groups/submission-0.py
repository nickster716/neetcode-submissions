class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        for i in range(len(strs)):
            if strs[i] == "0":
                continue
            anagramGroup = []
            anagramGroup.append(strs[i])
            for j in range(i+1, len(strs)):
               if len(strs[i]) == len(strs[j]) and self.isAnagram(strs[i], strs[j]):
                anagramGroup.append(strs[j])
                strs[j] = "0"
            
            answer.append(anagramGroup)
        
        return answer


    
    def isAnagram(self, s1, s2):
        if s1 == "0" or s2 == "0":
            return False
        dS1 = {}
        dS2 = {}
        for k in range(len(s1)):
            dS1[s1[k]] = 1 + dS1.get(s1[k],0)
            dS2[s2[k]] = 1 + dS2.get(s2[k],0)
        
        for char in dS1:
            if char not in dS2:
                return False
            elif dS1[char] != dS2[char]:
                return False
            
        return True
            