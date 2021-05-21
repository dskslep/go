import random

from dlgo.agent.base import Agent
from dlgo.goboard import Move
from dlgo.agent.helpers import legal_moves
MAX_SCORE = 1000


def best_result(state, depth, eval_fn):
    if state.is_over():
        if state.winner() == state.next_player:
            return MAX_SCORE
        else:
            return -MAX_SCORE
    elif depth == 0:
        return eval_fn(state)
    else:
        best_so_far = -MAX_SCORE

        for move in legal_moves(state):
            next_state = state.apply_move(move)
            opponent_best = best_result(next_state, depth-1, eval_fn)
            our_best = - opponent_best
            if our_best > best_so_far:
                best_so_far = our_best
            if best_so_far == MAX_SCORE:
                return best_so_far

        return best_so_far


def alpha_beta_best(state, alpha, depth, eval_fn):
    if state.is_over():
        if state.winner() == state.next_player:
            return MAX_SCORE
        else:
            return -MAX_SCORE
    elif depth == 0:
        return eval_fn(state)
    else:
        best_so_far = -MAX_SCORE
        for move in legal_moves(state):
            next_state = state.apply_move(move)
            opposite_result = alpha_beta_best(next_state, best_so_far, depth - 1, eval_fn)
            if opposite_result < alpha:
                return opposite_result
            our_result = - opposite_result

            if our_result > best_so_far:
                best_so_far = our_result

        return best_so_far


class MinimaxBot(Agent):
    def __init__(self, max_depth, eval_fn):
        super().__init__()
        self.max_depth = max_depth
        self.eval_fn = eval_fn

    def select_move(self, game_state):
        best_moves = []
        best_so_far = -MAX_SCORE
        for move in legal_moves(game_state):
            next_state = game_state.apply_move(move)
            opponent_best = alpha_beta_best(next_state, best_so_far, self.max_depth, self.eval_fn)
            # opponent_best = best_result(next_state, self.max_depth, self.eval_fn)

            our_result = -opponent_best
            if our_result > best_so_far:
                best_moves = [move]
                best_so_far = our_result
            elif our_result == best_so_far:
                best_moves.append(move)

        if not best_moves:
            return Move.pass_turn()
        return random.choice(best_moves)
