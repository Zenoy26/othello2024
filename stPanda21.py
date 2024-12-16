BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]



class AI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        return x, y



import math
import random

BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

def can_place_x_y(board, stone, x, y):
    """
    石を置けるかどうかを調べる関数。
    board: 2次元配列のオセロボード
    x, y: 石を置きたい座標 (0-indexed)
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 置けるなら True, 置けないなら False
    """
    if board[y][x] != 0:
        return False  # 既に石がある場合は置けない

    opponent = 3 - stone  # 相手の石 (1なら2、2なら1)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True  # 石を置ける条件を満たす

    return False

def can_place(board, stone):
    """
    石を置ける場所を調べる関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False

def random_place(board, stone):
    """
    石をランダムに置く関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    while True:
        x = random.randint(0, len(board[0]) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_x_y(board, stone, x, y):
            return x, y

class PandaAI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        x, y = random_place(board, stone)
        return x, y



def count_flips(board, stone, x, y):
    """
    指定された座標に石を置いたときに裏返せる石の数を数える。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    x, y: 石を置きたい座標 (0-indexed)
    return: 裏返せる石の数
    """
    if board[y][x] != 0:
        return 0  # 既に石がある場合は0

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    flip_count = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flips_in_direction = 0

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            flips_in_direction += 1

        if flips_in_direction > 0 and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            flip_count += flips_in_direction

    return flip_count


def best_place(board, stone):
    """
    石を置いたときに一番多くの石を裏返せる座標を見つける。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 最適な座標 (x, y)
    """
    max_flips = 0
    best_move = None

    for y in range(len(board)):
        for x in range(len(board[0])):
            flips = count_flips(board, stone, x, y)
            if flips > max_flips:
                max_flips = flips
                best_move = (x, y)

    return best_move


class EagerAI(object):

    def face(self):
        return "🐯"

    def place(self, board, stone):
        move = best_place(board, stone)
        if move:
            return move
        return random_place(board, stone)  # 万が一置ける場所がない場合


import random

# 評価表
EVALUATION_TABLE = [
    [30, -12, 0, -1, -1, 0, -12, 30],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [30, -12, 0, -1, -1, 0, -12, 30]
]

# 必要な補助関数
def can_place_x_y(board, stone, x, y):
    """
    指定された位置に石を置けるかどうかを判定する。
    """
    if board[y][x] != 0:  # 空きマスでない場合は置けない
        return False

    opponent = 3 - stone  # 相手の石
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        # 方向に沿って相手の石があるか確認
        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        # 自分の石で挟める場合は置ける
        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True

    return False

def get_legal_moves(board, stone):
    """
    現在の石の合法手をすべて取得する。
    """
    moves = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                moves.append((x, y))
    return moves

def evaluate_move(board, stone, x, y):
    """
    指定した座標に基づく手の評価値を計算。
    """
    return EVALUATION_TABLE[y][x]

# 強化されたAIクラス
class StrongPandaAI(object):

    def face(self):
        return "🐼💪"

    def place(self, board, stone):
        # すべての合法手を取得
        legal_moves = get_legal_moves(board, stone)

        if not legal_moves:
            return None  # 合法手がない場合はNoneを返す（パス）

        # 各合法手の評価値を計算
        best_move = None
        best_score = float('-inf')  # 初期値は非常に低い値
        for move in legal_moves:
            x, y = move
            score = evaluate_move(board, stone, x, y)
            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move




!pip install -U kogi-canvas



from kogi_canvas import play_othello, PandaAI


BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

play_othello(StrongPandaAI()) # ここを自分の作ったAIに変える

