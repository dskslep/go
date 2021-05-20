import random

from dlgo.agent.base import Agent
from dlgo.goboard import Move
from dlgo.agent.helpers import legal_moves


class RandomBot(Agent):
    def select_move(self, game_state):
        candidates = legal_moves(game_state)
        if not candidates:
            return Move.pass_turn()

        return random.choice(candidates)
