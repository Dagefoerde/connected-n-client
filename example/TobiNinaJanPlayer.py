""" Player implementation for TobiNinaJan"""

from py_client.player import Player


class TobiNinaJanPlayer(Player):
    def __init__(self, player):
        self._player = player

    def choose_action(self) -> int:
        return self._player.nextMove()

    def inform(self, column: int, opponent: bool):
        action = 1 if opponent else 0
        self._player.inform(action)
        pass

    def reset(self):
        # TODO
        pass