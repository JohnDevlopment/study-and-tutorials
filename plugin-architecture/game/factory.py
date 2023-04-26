from __future__ import annotations
from typing import Any, cast, Callable
from .character import GameCharacter

character_functions: dict[str, Callable[..., GameCharacter]] = {}

def register_character_type(name: str, fn: Callable[..., GameCharacter]):
    """Register a character type under NAME."""
    character_functions[name] = fn

def unregister_character_type(name: str):
    """Unregister a character type under NAME."""
    character_functions.pop(name, None)

def new_character(opts: dict[str, Any]) -> GameCharacter:
    """Create a game character of a certain type using OPTS."""
    opts_copy = opts.copy()
    character_type = opts_copy.pop("type")
    try:
        fn = character_functions[character_type]
        return fn(**opts_copy)
    except KeyError:
        raise ValueError(f"unknown character type {character_type!r}")
