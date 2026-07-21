class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = False
        freq = {}
        for num in nums:
            if num in freq:
                answer = True
                break
            else:
                freq[num] = 1
        
        return answer