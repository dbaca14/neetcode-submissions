class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):

                curr = board[i][j]
                if curr != '.':

                    # Row timestamp
                    rowTS = f"row_{i}_{curr}"
                    # Col timestamp
                    colTS = f"rcol_{j}_{curr}"
                    # Box timestamp
                    boxTS = f"box_{i//3}_{j//3}_{curr}"

                    if rowTS in seen or colTS in seen or boxTS in seen:
                        return False
                    seen.update([rowTS, colTS, boxTS])

        return True
