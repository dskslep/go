import random

from dlgo.agent.base import Agent
from dlgo.agent.naive import RandomBot
from dlgo.goboard import Move
from dlgo.agent.helpers import legal_moves
from dlgo.gotypes import Player
from dlgo.utils import print_board


class MCNode:
    def __init__(self, game_state, parent=None, move=None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.children = []

        self.win_count = {
            Player.black: 0,
            Player.white: 0
        }

        self.num_rollouts = 0
        self.unvisited_moves = legal_moves(game_state) + [Move.pass_turn()]

    def add_random_child(self):
        index = random.randint(0, len(self.unvisited_moves) - 1)
        new_move = self.unvisited_moves.pop(index)
        new_game_state = self.game_state.apply_move(new_move)
        new_node = MCNode(new_game_state, self, new_move)
        self.children.append(new_node)
        return new_node

    def record_win(self, winner):
        self.win_count[winner] += 1
        self.num_rollouts += 1

    def can_add_child(self):
        return len(self.unvisited_moves) > 0

    def is_terminal(self):
        return self.game_state.is_over()

    def winning_frac(self, player):
        return self.win_count[player] / self.num_rollouts

    def select_child(self):
        return random.choice(self.children)


def simulate_random_game(game_state):
    bot = RandomBot()
    while not game_state.is_over():
        bot_move = bot.select_move(game_state)
        game_state = game_state.apply_move(bot_move)
    return game_state.winner()


class MCBot(Agent):
    def __init__(self, num_rounds):
        super().__init__()
        self.num_rounds = num_rounds

    def select_move(self, game_state):
        root = MCNode(game_state)
        for i in range(self.num_rounds):
            node = root
            while (not node.can_add_child()) and (not node.is_terminal()):
                node = node.select_child()

            if node.can_add_child():
                node = node.add_random_child()

            winner = simulate_random_game(node.game_state)
            while node is not None:
                node.record_win(winner)
                node = node.parent

        best_move = None
        best_pct = -1
        for child in root.children:
            child_pct = child.winning_frac(game_state.next_player)
            if child_pct > best_pct:
                best_pct = child_pct
                best_move = child.move

        return best_move
