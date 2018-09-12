from collections import defaultdict
from enum import Enum

from typing import List, Dict


class Move(Enum):
    Defect = -1
    Collaborate = +1


class MovePair:
    def __init__(self):
        self.__for = None
        self.__to = None

    def update_for_player(self, move: Move):
        self.__for = Move

    def update_to_player(self, move: Move):
        self.__to = Move

    def get_pair(self) -> (Move, Move):
        return (self.__for, self.__to)


class MoveGrid:
    def __init__(self, grid_size: int):
        self.grid = [[None for _ in range(grid_size)]
                     for _ in range(grid_size)]

    def get_move_pair(self, for_player: int, to_player: int) -> MovePair:
        move_pair = self.grid[for_player][to_player]
        if not move_pair:
            move_pair = MovePair()

        return move_pair

    def update_moves(self, for_player: int, to_player: int, move: Move):
        move_pair = self.get_move_pair(for_player, to_player)
        move_pair.update_for_player(move)

        move_pair = self.get_move_pair(to_player, for_player)
        move_pair.update_to_player(move)


class Player:
    pass


class ScoreEngine:
    pass


class Arbiter:
    """
    Arbiter is responsible for:
    * Maintaining history of moves
    * Taking input from all players and updating the status of current round
    * Keeping track of scores for all players
    * Keeping track of rounds
    * Triggering each player to return moves for each round
    """

    def __init__(self, engine: ScoreEngine, total_rounds: int = 200):
        self.__round = 1
        self.__moves = {}
        self.__moves_in_round = []
        self.__players = {}
        self.__scores = defaultdict(list)
        self.__total_rounds = total_rounds

    def subscribe_player(self, player: Player):
        self.__players[len(self.__players) + 1] = player

    def subscribe_players(self, players: List[Player]):
        for player in players:
            self.subscribe_player(player)

    def process_moves_from_player(self, player: Player,
                                  moves: Dict[Player, Move]):
        for player_id, move in moves.items():
            self.update_move_per_player(player, player_id, move)

    def update_move_per_player(self, player: Player, player_id: int,
                               move: Move):
        pass

    def start_round(self):
        pass

    def end_round(self):
        pass

    def has_round_finished(self) -> bool:
        pass
