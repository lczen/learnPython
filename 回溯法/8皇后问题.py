class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        ans = []

        def isValid(r, c):
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            return True

        def traceback(i):
            if i == n:
                temp = []
                for x in board:
                    temp.append("".join(x))
                ans.append(temp)
                return

            for j in range(n):
                if isValid(i, j):
                    # print(i,j)
                    board[i][j] = 'Q'
                    # print(board)
                    traceback(i + 1)
                    board[i][j] = '.'

        traceback(0)
        return ans