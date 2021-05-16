from dlgo.agent.helpers import is_point_an_eye
from dlgo.agent.naive import RandomBot
from dlgo.goboard_slow import GameState, Move
from dlgo.gotypes import Player
from dlgo.utils import print_board, print_move, point_from_coords


def main():
    board_size = 4
    game = GameState.new_game(board_size)
    bot = RandomBot()
    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)

        if game.next_player == Player.black:
            valid = False
            while not valid:
                human_move = input('-- ')
                point = point_from_coords(human_move.strip())
                move = Move.play(point)
                valid = game.is_valid_move(move)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
