import random
from gotypes import Player, Point


def to_python(player_state):
    if player_state is None:
        return 'None'
    else:
        return str(player_state)


MAX63 = 0x7ffffffffffffffff

table = {}
empty_board = 0
for row in range(1, 20):
    for col in range(1, 20):
        code = random.randint(0, MAX63)
        table[Point(row, col), None] = code
        empty_board += code
        for state in (Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code


with open('dlgo/zobrist.py', 'w') as f:
    f.writelines('''from dlgo.gotypes import Player, Point

__all__ = ['HASH_CODE', 'EMPTY_BOARD']

HASH_CODE = {
''')

    for (pt, state), hashcode in table.items():
        f.writelines(f'   ({pt}, {str(state)}): {hashcode},\n')

    f.writelines(f'''{"}"}

EMPTY_BOARD = {empty_board}
''')


