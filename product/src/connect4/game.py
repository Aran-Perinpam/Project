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

    def switch_player(self) -> None:
        # swaps the current player
        self.current_player = 2 if self.current_player == 1 else 1
