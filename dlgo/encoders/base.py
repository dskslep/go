import importlib


class Encoder:
    def name(self):
        raise NotImplemented

    def encode(self, game_state):
        raise NotImplemented

    def encode_point(self, point):
        raise NotImplemented

    def decode_point_index(self, index):
        raise NotImplemented

    def num_points(self):
        raise NotImplemented

    def shape(self):
        raise NotImplemented



