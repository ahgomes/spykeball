"""Current Testing Suite."""

from spykeball.player import Player
from spykeball.game import Game

P1 = Player("Billy")
P2 = Player("Bobby")
P3 = Player("Max")
P4 = Player("Cole")

G1 = Game(P1, P2, P3, P4)