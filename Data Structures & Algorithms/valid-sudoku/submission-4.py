class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # validate rows

        for i in range(9):
            row = set()
            for j in range(9):
                curr = board[i][j]
                if curr != ".":
                    if curr in row:
                        return False 
                    row.add(curr)

                
        # validate columns
        for i in range(9):
            col = set()
            for j in range(9):
                curr = board[j][i]
                if curr != ".":
                    if curr in col:
                        return False
                    col.add(curr)

        # validate boxes
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        for i, j in starts:
            s = set()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    item = board[x][y]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True


