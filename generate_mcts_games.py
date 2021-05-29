import argparse
import numpy as np

from dlgo.encoders import get_encoder_by_name
from dlgo import goboard_fast as goboard
from dlgo.agent.montecarlo import MCBot

from dlgo.utils import print_board, print_move


def generate_game(board_size, rounds, max_moves):
    boards, moves = [], []
    encoder = get_encoder_by_name('oneplane', board_size)
    game = goboard.GameState.new_game(board_size)
    bot = MCBot(rounds)
    num_moves = 0
    while not game.is_over():
        move = bot.select_move(game)
        if move.is_play():
            boards.append(encoder.encode(game))
            move_one_hot = np.zeros(encoder.num_points())
            move_one_hot[encoder.encode_point(move.point)] = 1
            moves.append(move_one_hot)
        game = game.apply_move(move)
        num_moves += 1
        if num_moves > max_moves:
            break

    return np.array(boards), np.array(moves)


if __name__ == '__main__':
    pass