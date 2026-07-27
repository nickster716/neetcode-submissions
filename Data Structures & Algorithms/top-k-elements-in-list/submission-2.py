class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # tc : O(n) 
        # sc: O(n)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        
        freqList = [[] for i in range(len(nums)+1)]
        for num,count in freq.items():
            freqList[count].append(num)
        
        answer=[]
        for i in range(len(freqList)-1, 0 , -1):
            for n in freqList[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
