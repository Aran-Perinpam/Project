import sys
import pygame

from connect4.game import Connect4Game


# draws the current connect four board
def main() -> None:
    pygame.init()

    game = Connect4Game()

    winner = 0
    draw = False
    cell_size = 90
    margin = 20
    width = margin * 2 + game.cols * cell_size
    height = margin * 2 + game.rows * cell_size + 60 

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Connect Four")

    font = pygame.font.SysFont(None, 32)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # press r to reset the board
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game.reset()
                winner = 0
                draw = False

            # checks that the game has not been won before letting the players make an action
            if winner == 0 and not draw:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos

                    grid_left = margin
                    grid_top = margin
                    grid_right = margin + game.cols * cell_size
                    grid_bottom = margin + game.rows * cell_size

                    if grid_left <= mouse_x < grid_right and grid_top <= mouse_y < grid_bottom:
                        col = (mouse_x - margin) // cell_size

                        # checks if a column is full before an action
                        if not game.is_column_full(col):
                            game.drop_disc(col)

                            # check if the game has ended before switching player
                            winner = game.check_winner()
                            if winner == 0:
                                draw = game.is_draw()
                                if not draw:
                                    game.switch_player()

        # clear block background
        screen.fill((20, 20, 20))

        # displays who's turn it is
        if winner != 0:
            message = f"player {winner} wins! press R to restart"
        elif draw:
            message = "draw! press R to restart"
        else:
            message = f"player {game.current_player}'s turn"

        text = font.render(message, True, (240, 240, 240))
        screen.blit(text, (margin, height - 50))

        # draws grid and disc spaces
        for r in range(game.rows):
            for c in range(game.cols):
                x = margin + c * cell_size
                y = margin + r * cell_size

                pygame.draw.rect(screen, (30, 30, 160), (x, y, cell_size, cell_size))

                center = (x + cell_size // 2, y + cell_size // 2)
                value = game.board[r][c]

                if value == 1:
                    colour = (220, 60, 60)
                elif value == 2:
                    colour = (240, 220, 60)
                else:
                    colour = (25, 25, 25)

                pygame.draw.circle(screen, colour, center, cell_size // 2 - 8)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
