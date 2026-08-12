class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # tc O(n) and sc O(n)
        l = 0
        freqMap = {}
        maxFreq = 0
        longestSL = 0
        r=0
        while r < len(s):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxFreq = max(maxFreq, freqMap[s[r]])

            windowLength = r-l+1
            if windowLength - maxFreq <= k:
                longestSL = max(longestSL, windowLength)
                r+=1
            else:
                freqMap[s[l]] -=1
                l+=1
                # freqMap[s[r]] -=1
                # maxFreq = max(maxFreq, freqMap[s[r]])

                windowLength = r-l+1
                if windowLength - maxFreq <= k:
                    longestSL = max(longestSL, windowLength)
                    r+=1

        return longestSL