class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        l= 0
        r= 1

        while r< len(s) and s[l] == s[r]:
            l+=1
            r+=1
        
        if r == len(s):
            longestS = 1
            # print("12",longestS)
            return longestS
        else:
            longestS = 2

        freqMap = {
            s[l] : 1,
            s[r] : 1
        }

        r+=1
        while r < len(s):
            if s[r] in freqMap:
                del freqMap[s[l]]
                l = l+1
                # r = l+1
                # while r< len(s) and s[l] == s[r]:
                #     l+=1
                    # r+=1
                # if r == len(s):
                #     break
                # freqMap = {
                #     s[l] : 1,
                #     s[r] : 1
                # }
                # longestS = max(longestS, len(freqMap.keys()))
                # print("39", longestS, freqMap)

                # r+=1
            else:
                freqMap[s[r]] = 1
                # print("r",r, "freqMap", freqMap)
                longestS = max(longestS, len(freqMap.keys()))
                # print("44", longestS, freqMap)
                r+=1
        
        return longestS