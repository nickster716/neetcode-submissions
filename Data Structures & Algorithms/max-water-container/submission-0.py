class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights)-1
        maxArea = 0
        while i<j:
            containerHeight = min(heights[i],heights[j])
            length = j-i
            area = length* containerHeight
            maxArea = max(maxArea, area)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return maxArea