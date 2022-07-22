class Move:

    ranksToRow = {"1":7, "2":6, "3":5, "4": 4, "5":3, "6": 2, "7": 1, "8": 0}
    rowsToRank = {v:k for k,v in ranksToRow.items()}
    filesToCols = {"a":0, "b":1, "c":2, "d":3, "e": 4, "f":5, "g":6, "h": 7}
    colsToFiles = {v:k for k,v in filesToCols.items()}

    def __init__(self, start_square, end_square, board):
        self.board = board
        self.start_row, self.start_col = start_square
        self.end_row, self.end_col = end_square
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
    
    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r,c):
        return self.colsToFiles[c] + self.rowsToRank[r]


class GameState:
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]

        self.whiteToMove = True
        self.moveLog = []

    def make_move(self, move: Move):
        self.board[move.start_row][move.start_col] = '--'
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


