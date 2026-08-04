class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [ [0] * cols for _ in range(rows) ]
        maxValue = 0

        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1, -1):
                matrixValue = int(matrix[i][j])
                if matrixValue == 0:
                    dp[i][j] = 0
                    continue
                right = 0
                diagonal = 0
                bottom = 0
                if (j+1) < cols:
                    right = dp[i][j+1]
                if (i+1)< rows and (j+1)< cols:
                    diagonal = dp[i+1][j+1]
                if (i+1) < rows:
                    bottom = dp[i+1][j]
                
                dp[i][j] = min(right,diagonal,bottom) + 1
                maxValue = max(maxValue,dp[i][j])
        
        largestSq = maxValue * maxValue
        return largestSq

                
                
