from connect4.game import Connect4Game


# tests for each type of win
def test_horizontal() -> bool:
    g = Connect4Game()
    # creates a board with a horizontal win
    for col in [0, 1, 2, 3]:
        g.drop_disc(col)
    return g.check_winner() == 1


def test_vertical() -> bool:
    g = Connect4Game()
    # creates a board with a veritical win
    for _ in range(4):
        g.drop_disc(0)
    return g.check_winner() == 1


def test_diagonal_down_right() -> bool:
    g = Connect4Game()

    # creates a board with a diagonal down right win
    g.board[2][0] = 1
    g.board[3][1] = 1
    g.board[4][2] = 1
    g.board[5][3] = 1

    return g.check_winner() == 1



def main() -> None:
    results = {
        "horizontal": test_horizontal(),
        "vertical": test_vertical(),
        "diagonal": test_diagonal_down_right(),
    }

    for name, ok in results.items():
        print(name, "pass" if ok else "fail")

    if all(results.values()):
        print("check: pass")
    else:
        print("check: fail")


if __name__ == "__main__":
    main()
