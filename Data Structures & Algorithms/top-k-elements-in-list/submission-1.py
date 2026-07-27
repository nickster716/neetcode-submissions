class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        
        heap = []
        for num,count in freq.items():
            heapq.heappush(heap, (count,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        answer = []
        while heap:
            count, num = heapq.heappop(heap)
            answer.append(num)
        
        return answer
