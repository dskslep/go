from dlgo.gotypes import Point
from dlgo.goboard_fast import Move


def is_point_an_eye(board, point, color):
    if board.get(point) is not None:
        return False

    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False

    friendly_corners = 0
    off_board_corners = 0

    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]

    for corner in corners:
        if not board.is_on_grid(corner):
            off_board_corners += 1
        else:
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1
    if off_board_corners > 0:
        return off_board_corners + friendly_corners == 4

    return friendly_corners >= 3


def legal_moves(state):
    candidates = []
    for r in range(1, state.board.num_rows + 1):
        for c in range(1, state.board.num_cols + 1):
            candidate = Move.play(Point(row=r, col=c))
            if state.is_valid_move(candidate) \
                    and not is_point_an_eye(state.board, candidate.point, state.next_player):
                candidates.append(candidate)
    return candidates
