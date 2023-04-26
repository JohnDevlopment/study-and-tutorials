#!/usr/bin/env python3

"""
Plugin architecture example.

This code is adaped from the example of plugin architecture
from the Youtube channel ArjanCodes. His license is included
in this very directory.

-- ArjanCodes --
Video source: https://www.youtube.com/watch?v=iCE1bDoit9Q
Github: https://github.com/ArjanCodes/2021-plugin-architecture

-- Me --
Github: https://github.com/JohnDevlopment/study-and-tutorials/add plugin-architecture
"""

from __future__ import annotations
from dataclasses import dataclass
from game import factory, loader
import json

@dataclass
class Knight:
    name: str
    hp: int = -1

    def make_a_noise(self):
        print(f"Raaah! I am {self.name}, son of so-and-so!")

@dataclass
class Assassin:
    name: str
    hp: int

    def make_a_noise(self):
        print(f"Hehehehe. (I, {self.name}, will make a name for myself with this kill.)")

def main ():
    """Creates one or more game characters based on a level definition."""

    # Register character types with the factory
    factory.register_character_type("knight", Knight)
    factory.register_character_type("assassin", Assassin)

    with open("level.json") as fd:
        data = json.load(fd)

    # Load plugins
    loader.load_plugins(data["plugins"])

    # Formerly:
    # characters: list[GameCharacter] = []
    # for item in data['characters']:
    #     item_copy = cast(dict[str, Any], item).copy()
    #     character_type: str = item_copy.pop('type')
    #     match character_type:
    #         case "knight":
    #             characters.append(Knight(**item_copy))
    #         case "assassin":
    #             characters.append(Assassin(**item_copy))
    #         case other:
    #             raise ValueError(f"invalid character type {other}")
    # Now:
    characters = [factory.new_character(item) for item in data["characters"]]

    # We change the above code to use a factory to create characters
    # of specified types. Factories are probably a key element in
    # plugin architecture, because they are what allow the creation
    # of, say, characters without having to know the details in here.

    for char in characters:
        print(char, end="\t")
        char.make_a_noise()

if __name__ == "__main__":
    main()
