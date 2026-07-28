class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        curr = 1
        for i in range(len(nums)):
            prefix[i] = curr
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums)-1 , -1 , -1):
            suffix[i] = curr
            curr *= nums[i]
        
        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])

        return answer
