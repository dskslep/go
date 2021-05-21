import time

from dlgo.agent.minimax import MinimaxBot
from dlgo.agent.montecarlo import MCBot
from dlgo.agent.naive import RandomBot
from dlgo.goboard import GameState
from dlgo.gotypes import Player
from dlgo.utils import print_board, print_move, capture_diff


def main():
    board_size = 4
    results = {}
    start = time.time()

    for i in range(10):
        game = GameState.new_game(board_size)
        bots = {
            Player.black: RandomBot(),# MinimaxBot(2, capture_diff),
            Player.white: MCBot(30),
        }
        while not game.is_over():
            # time.sleep(0.1)
            # print(chr(27) + "[2J")
            # print_board(game.board)
            bot_move = bots[game.next_player].select_move(game)
            # print_move(game.next_player, bot_move)
            game = game.apply_move(bot_move)
        if capture_diff(game) > 0:
            results[game.next_player] = results.get(game.next_player, 0) + 1
        elif capture_diff(game) < 0:
            results[game.next_player.other] = results.get(game.next_player.other, 0) + 1
        # print(game.next_player, capture_diff(game))
    print(results, time.time() - start)


if __name__ == '__main__':
    main()
