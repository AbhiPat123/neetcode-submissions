class Solution:
    def has_dupe(self, r_):
        r_ = [itm for itm in r_ if itm != "."]
        return len(r_) != len(set(r_))

    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        # lets go through row
        for r in range(len(board)):
            board_row = board[r]
            if self.has_dupe(board_row):
                return False

        # lets go through each column
        for c in range(len(board)):
            board_col = [board[r][c] for r in range(9)]
            if self.has_dupe(board_col):
                return False

        # lets go through each box
        for b in range(len(board)):
            i_list = range((b//3)*3,((b//3)*3)+3)
            j_list = range((b%3)*3,(b%3)*3+3)
            board_box = [board[i][j] for i,j in zip(i_list,j_list)]
            if self.has_dupe(board_box):
                return False

        return True

        


