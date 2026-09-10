class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[i][j]
                if curr in seen:
                    return False
                elif curr != '.':
                    seen.add(curr)
                
        # Check columns 
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[j][i]
                if curr in seen:
                    return False
                elif curr != '.':
                    seen.add(curr)
        
        # Check boxes
        starts = [ (0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6),
                ]
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    curr = board[row][col]
                    if curr in s:
                        return False
                    elif curr != '.':
                        s.add(curr)

        return True
