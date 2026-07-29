class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # tc O(1) and sc O(1)

        # each row and col traversal
        for row in range(9):
            drow = {}
            dcol = {}
            for col in range(9):
                if board[row][col] != '.':
                    numInRow = board[row][col]
                    drow[numInRow] = 1 + drow.get(numInRow, 0)
                    if drow[numInRow] > 1:
                        print("row failed")
                        return False
                
                if board[col][row] != '.':
                    numInCol = board[col][row]
                    dcol[numInCol] = 1 + dcol.get(numInCol, 0)
                    if dcol[numInCol] > 1:
                        
                        return False

            # print("drow",drow, "row", row)
            # print("dcol",dcol, "col", row)

        # the 9 sub box traversal   
        nineBoxes = [[0,2], [3,5], [6,8]]
        for a in nineBoxes:
            for b in nineBoxes:
                dSubBox = {}
                for i in range(a[0],a[1]+1):
                    for j in range(b[0], b[1]+1):
                        if board[i][j] == '.':
                            continue
                        num = board[i][j]
                        dSubBox[num] = 1 + dSubBox.get(num,0)
                        if dSubBox[num] > 1:
                            print("sub box failed")
                            return False
                
                # print("dSubBox", dSubBox)
        
        return True