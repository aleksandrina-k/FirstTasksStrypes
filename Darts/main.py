def create_darts_board():
    board = [x for x in range(1, 21)] \
            + [2 * x for x in range(1, 21)] \
            + [3 * x for x in range(1, 21)] \
            + [25, 50]
    board = list(set(board))
    board.sort(reverse=True)

    return board


# def shooting_1(points):
#     result = []
#
#     #  searching for perfect move
#     if points in DARTS and points % 2 == 0 and (points <= 40 or points == 50):
#         return f'Perfect score: {[points]}'
#
#     #  there isn't perfect move
#     #  searching for maximum points
#     if points in DARTS:
#         return f'Maximum points: {[points]}'
#
#     for k in DARTS:
#         if k < points:
#             return f'Maximum points: {[k]}'
#
#     return None
#
#
# def shooting_2(points):
#     result = []
#
#     for j in DARTS:
#         for k in DARTS:
#             if (k % 2 == 0 and (k <= 40 or k == 50)) and j + k == points:
#                 result.extend([j, k])
#                 return f'Perfect score: {result}'
#
#     #  the player can't finish the game
#     #  searching maximum points
#     for j in DARTS:
#         for k in DARTS:
#             if j + k == points:
#                 result.extend([j, k])
#                 return f'Maximum points: {result}'
#
#     return f'Maximum points: {2 * DARTS[0]}'
#
#
# def shooting_3(points):
#     result = []
#
#     for i in DARTS:
#         for j in DARTS:
#             for k in DARTS:
#                 if (k % 2 == 0 and (k <= 40 or k == 50)) and i + j + k == points:
#                     result.extend([i, j, k])
#                     return f'Perfect score: {result}'
#
#     #  the player can't finish the game
#     #  searching maximum points
#     for i in DARTS:
#         for j in DARTS:
#             for k in DARTS:
#                 if i + j + k == points:
#                     result.extend([i, j, k])
#                     return f'Maximum points: {result}'
#
#     return f'Maximum points: {3 * DARTS[0]}'


# perfect_move(3, 150, [])
# if nr_darts == 1:
#     return shooting_1(current_points)
#
# elif nr_darts == 2:
#     return shooting_2(current_points)
#
# else:
#     return shooting_3(current_points)

from itertools import combinations


def perfect_move_comb(nr_darts: int, current_points):
    assert 0 < nr_darts <= 3, "Darts arrows must be greater than 0 and less than 3."
    assert current_points > 0, "Points must be greater than 0."

    darts_board = create_darts_board()
    all_combinations = list(combinations(darts_board, nr_darts))

    for combination in all_combinations:
        if combination[-1] % 2 == 0 and (combination[-1] <= 40 or combination[-1] == 50) and sum(
                combination) == current_points:
            return [combination]

    return None


DARTS = create_darts_board()

if __name__ == '__main__':
    arrows = int(input())
    current_points = int(input())

    # print(perfect_move(arrows, current_points))
    print(perfect_move_comb(arrows, current_points))
