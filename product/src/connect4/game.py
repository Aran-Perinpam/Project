from __future__ import annotations

from dataclasses import dataclass


# outlines the game rules
# ensures the board is empty to begin with and when it resets
@dataclass
class Connect4Game:
    rows: int = 6
    cols: int = 7

    def __post_init__(self) -> None:
        # 0 = empty cell
        # 1 = player 1 piece
        # 2 = player 2 piece
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 1

    def reset(self) -> None:
        # resets the board back to empty
        # player 1 starts again
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 1

    def legal_moves(self) -> list[int]:
        # allowed to play a move it the top cell is empty
        return [c for c in range(self.cols) if self.board[0][c] == 0]

    def drop_disc(self, col: int) -> int:
        # when a move is made, returns the row the piece fall to
        if col not in self.legal_moves():
            raise ValueError(f"illegal move: {col}")

        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = self.current_player
                return r

        raise RuntimeError("column was unexpectedly full")
    
    def is_column_full(self, col: int) -> bool:
        # if the top cell is not empty, the column is full
        if col < 0 or col >= self.cols:
            raise ValueError(f"invalid column: {col}")
        return self.board[0][col] != 0

    def switch_player(self) -> None:
        # swaps the current player
        self.current_player = 2 if self.current_player == 1 else 1

    def check_winner(self) -> int:
        # returns 0 if there is no winner
        # returns either 1 or 2 if the respective player has won
        b = self.board

        # checks horizontal wins
        for r in range(self.rows):
            for c in range(self.cols - 3):
                p = b[r][c]
                if p != 0 and p == b[r][c + 1] == b[r][c + 2] == b[r][c + 3]:
                    return p

        # checks vertical wins
        for r in range(self.rows - 3):
            for c in range(self.cols):
                p = b[r][c]
                if p != 0 and p == b[r + 1][c] == b[r + 2][c] == b[r + 3][c]:
                    return p

        # checks wins pointing diagonally down to the right
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                p = b[r][c]
                if p != 0 and p == b[r + 1][c + 1] == b[r + 2][c + 2] == b[r + 3][c + 3]:
                    return p

        # checks wins pointing diagonally up to the right
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                p = b[r][c]
                if p != 0 and p == b[r - 1][c + 1] == b[r - 2][c + 2] == b[r - 3][c + 3]:
                    return p

        return 0

    def is_draw(self) -> bool:
        # when the board is full and there is no winner, returns a draw
        return self.check_winner() == 0 and len(self.legal_moves()) == 0

