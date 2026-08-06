class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l] , height[r]
        result = 0

        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                waterHeightAtCurrL = leftMax - height[l]
                if waterHeightAtCurrL > 0:
                    result+= waterHeightAtCurrL
            
            # elif rightMax < leftMax:
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                waterHeightAtCurrR = rightMax - height[r]
                if waterHeightAtCurrR > 0:
                    result+= waterHeightAtCurrR
        
        return result
                


