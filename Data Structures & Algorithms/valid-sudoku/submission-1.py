class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dsmallbox = {}
        for i in range(9):
            drow = {}
            dcol = {}
            for j in range(9):
                if board[i][j] != '.':
                    numInRow = board[i][j]
                    drow[numInRow] = 1 + drow.get(numInRow, 0)
                    if drow[numInRow] > 1:
                        print("row failed")
                        return False
                
                if board[j][i] != '.':
                    numInCol = board[j][i]
                    dcol[numInCol] = 1 + dcol.get(numInCol, 0)
                    if dcol[numInCol] > 1:
                        print("col failed")
                        return False
                
                if board[i][j] == ".":
                    continue
                
                key = (i//3, j//3)
                num = board[i][j]
                if key not in dsmallbox:
                    dsmallbox[key] = {}
                    dsmallbox[key][num] = 1
                else:
                    hashSet = dsmallbox[key]
                    if num in hashSet:
                        print("small box failed")
                        return False
                    else:
                        hashSet[num] = 1
        
        return True
                    
                
               
                


