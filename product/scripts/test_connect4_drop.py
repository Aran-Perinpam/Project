from connect4.game import Connect4Game


# testing if pieces fall to the bottom available row
def main() -> None:
    game = Connect4Game()

    # discs dropped into the same row
    r1 = game.drop_disc(3)
    game.switch_player()
    r2 = game.drop_disc(3)
    game.switch_player()
    r3 = game.drop_disc(3)

    print("rows landed:", r1, r2, r3)
    print("expected:", 5, 4, 3)

    if (r1, r2, r3) == (5, 4, 3):
        print("check: pass")
    else:
        print("check: fail")


if __name__ == "__main__":
    main()
