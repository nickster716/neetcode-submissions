class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curr = 0
        longest = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr+=1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                longest = max(longest, curr+1)
                curr = 0
        
        longest = max(longest, curr+1)
        return longest