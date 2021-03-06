from dlgo.agent.minimax import MinimaxBot
from dlgo.goboard_fast import GameState, Move
from dlgo.gotypes import Player
from dlgo.utils import print_board, print_move, point_from_coords, capture_diff


def main():
    board_size = 4
    game = GameState.new_game(board_size)
    bot = MinimaxBot(5, capture_diff)
    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)

        if game.next_player == Player.black:
            valid = False
            while not valid:
                human_move = input('-- ')
                human_move = human_move.upper()
                point = point_from_coords(human_move.strip())
                move = Move.play(point)
                valid = game.is_valid_move(move)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
