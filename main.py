from checkerboard import CheckerBoard




if __name__ == "__main__":
    board = CheckerBoard(8)
    board.print_board()
    print('-----------------------------------')
    board.simulate_move((5, 0), (4, 1))
    board.print_board()
    print('-----------------------------------')
    board.simulate_move((5, 2), (4, 1))
    board.print_board()
    print('-----------------------------------')
    board.simulate_move((2, 3), (3, 2))
    board.print_board()
    print('-----------------------------------')
    board.simulate_move((4, 1), (2, 3))
    board.print_board()
    print(board.whites_remain)
    print(board.blacks_remain)
    # print('-----------------------------------')
    # board.simulate_move((1, 2), (3, 4))
    # board.print_board()


