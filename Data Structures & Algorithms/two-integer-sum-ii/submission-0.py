class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for index,num in enumerate(numbers):
            if target-num in d:
                return [d[target-num], index+1]
            else:
                d[num] = index+1