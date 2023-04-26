"""Plugin that adds a warlord character type."""

from __future__ import annotations
from dataclasses import dataclass
from game import factory

@dataclass
class Warlord:
    name: str
    hp: int
    territory: str

    def make_a_noise(self):
        print(f"I am Lord {self.name}! I own the territory of {self.territory}!")

def initialize():
    factory.register_character_type("warlord", Warlord)
