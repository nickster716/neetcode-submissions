class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        

        while k!=0:
            max = 0
            maxKey = -1
            for key in freq.keys():
                if freq[key] > max:
                    max = freq[key]
                    maxKey = key
            
            freq[maxKey] = -1
            answer.append(maxKey)
            k-=1
        
        return answer

            
                