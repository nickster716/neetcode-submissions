class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        
        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])

        for j in range(len(height)-2,0,-1):
            rightMax[j] = max(rightMax[j+1], height[j+1])

        result = 0
        for i in range(len(height)):
            waterHeight = min(leftMax[i],rightMax[i]) - height[i]
            if waterHeight > 0:
                result += waterHeight
        
        return result