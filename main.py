# IMPORTS
from checkerboard import CheckerBoard
from checkers import WIDTH, HEIGHT
import pygame

# Frames per second for the game playing rate
FPS = 60

# Initialize the game window
window_size = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(window_size)

# Name of the game
pygame.display.set_caption('Checkers Game')


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    # Quit the entire game
    pygame.quit()


main()



#############################################
################### MISC ####################
#############################################

# # Initialize Pygame
# pygame.init()
#
# # Set up the game window
# WINDOW_SIZE = (500, 500)
# screen = pygame.display.set_mode(WINDOW_SIZE)
#
# # Set up the game loop
# game_running = True
# checker_board = CheckerBoard(n=8)
# # Set up the colors
# PALE_WHITE = (255, 255, 204)
# LIGHT_BROWN = (204, 102, 0)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)
#
#
#
# while game_running:
#
#     # Draw the game graphics
#     CELL_SIZE = WINDOW_SIZE[0] // checker_board.n  # set the cell size to fit 8 rows
#     RADIUS = (CELL_SIZE // 2) - 10  # set the radius of the checkers
#
#     # Handle user input
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Check if the user clicked on a valid checker to select it
#             x, y = event.pos
#             row = y // CELL_SIZE
#             col = x // CELL_SIZE
#             checker = checker_board.board[row][col]
#             if checker != "" and not checker.is_captured and checker.get_color == (
#             "B" if len(valid_moves) % 2 == 0 else "W"):
#                 selected_checker = checker
#                 valid_moves = checker_board.get_valid_moves(checker)
#
#             # Check if the user clicked on a valid move to move the selected checker
#             elif selected_checker is not None and (row, col) in valid_moves:
#                 checker_board.move_checker(selected_checker.get_position(), (row, col))
#                 selected_checker = None
#                 valid_moves = []
#
#     # Update the game state
#     for row in range(checker_board.n):
#         for col in range(checker_board.n):
#             if (row + col) % 2 == 0:
#                 color = PALE_WHITE
#             else:
#                 color = LIGHT_BROWN
#             pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
#             checker = checker_board.board[row][col]
#             if checker != "" and not checker.is_captured:
#                 if checker.get_color == "W":
#                     color = RED
#                 else:
#                     color = BLACK
#                 pygame.draw.circle(screen, color, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), RADIUS)
#
#     pygame.display.flip()  # update the screen
#
#
# # Clean up Pygame
# pygame.quit()
#
#
# # if __name__ == "__main__":
# #     board = CheckerBoard(8)
# #     board.print_board()
# #     print('-----------------------------------')
# #     board.simulate_move((5, 0), (4, 1))
# #     board.print_board()
# #     print('-----------------------------------')
# #     board.simulate_move((5, 2), (4, 1))
# #     board.print_board()
# #     print('-----------------------------------')
# #     board.simulate_move((2, 3), (3, 2))
# #     board.print_board()
# #     print('-----------------------------------')
# #     board.simulate_move((4, 1), (2, 3))
# #     board.print_board()
# #     print(board.whites_remain)
# #     print(board.blacks_remain)
# #     # print('-----------------------------------')
# #     # board.simulate_move((1, 2), (3, 4))
# #     # board.print_board()


