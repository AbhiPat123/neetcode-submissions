from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_dict = defaultdict(set)
        c_dict = defaultdict(set)
        b_dict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell_num = board[r][c]
                if cell_num == ".":
                    continue
                # row check
                if cell_num in r_dict[r]:
                    return False
                else:
                    r_dict[r].add(cell_num)

                # col check
                if cell_num in c_dict[c]:
                    return False
                else:
                    c_dict[c].add(cell_num)

                # box check
                b = ((r//3)*3) + (c//3)
                if cell_num in b_dict[b]:
                    return False
                else:
                    b_dict[b].add(cell_num)

        return True