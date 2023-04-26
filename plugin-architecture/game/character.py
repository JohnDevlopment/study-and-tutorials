from __future__ import annotations
from typing import Protocol

class GameCharacter(Protocol):
    """Basic representation of a game character."""

    def make_a_noise(self) -> None:
        """Make a noise."""
        ...
