import numpy as np

from dlgo.encoders.base import Encoder
from dlgo.goboard_fast import Point


class OnePlaneEncoder(Encoder):
    def __init__(self, board_size):
        self.board_width, self.board_height = board_size
        self.num_planes = 1

    def name(self):
        return 'oneplane'

    def encode(self, game_state):
        board_matrix = np.zeros(self.shape())
        next_player = game_state.next_player
        for r in range(self.board_height):
            for c in range(self.board_width):
                point = Point(row=r, col=c)
                color = game_state.get(point)
                if color is None:
                    continue
                if color == next_player:
                    board_matrix[0, r, c] = 1
                else:
                    board_matrix[0, r, c] = -1

    def encode_point(self, point):
        return self.board_width * (point.row - 1) + point.col - 1

    def decode_point_index(self, index):
        row = index // self.board_width
        col = index % self.board_width

        return Point(row=row + 1, col=col + 1)

    def num_points(self):
        return self.board_width * self.board_height

    def shape(self):
        return self.num_planes, self.board_height, self.board_width
