import time

from dlgo.agent.minimax import MinimaxBot, MAX_SCORE
from dlgo.agent.naive import RandomBot
from dlgo.goboard import GameState
from dlgo.gotypes import Player
from dlgo.utils import print_board, print_move, capture_diff


def main():
    board_size = 4
    game = GameState.new_game(board_size)
    bots = {
        Player.black: MinimaxBot(3, capture_diff),
        Player.white: RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.1)
        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
    print(game.next_player, capture_diff(game))


if __name__ == '__main__':
    main()
