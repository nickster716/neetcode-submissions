class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countOfZero = 0

        answer = []
        for num in nums:
            if num == 0:
                countOfZero +=1
            else:
                product *= num
        
        if countOfZero > 1 : return [0]*len(nums)
        elif countOfZero == 1:
            for num in nums:
                if num == 0 :
                    answer.append(product)
                else:
                    answer.append(0)
        else:
            for num in nums:
                answer.append(product // num)
        
        return answer