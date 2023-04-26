"""Plugin loader."""

from __future__ import annotations
from typing import Protocol, cast
from . import factory
import importlib

class LoaderError(RuntimeError):
    """Error with the plugin loader."""

class PluginInterface(Protocol):
    """Interface to a plugin."""

    @staticmethod
    def initialize() -> None:
        """Initialize the plugin."""
        ...

def import_module(name: str) -> PluginInterface:
    """Dynamically load a module with the given name."""
    module = cast(PluginInterface, importlib.import_module(name))
    attr = getattr(module, "initialize", None)
    if attr is None or not callable(attr):
        raise LoaderError("missing or invalid attribute 'initialize', must exist and be a function.")
    return module

def load_plugins(plugins: list[str]) -> None:
    """Load the plugins defined in a list."""
    for pln in plugins:
        plugin = import_module(pln)
        plugin.initialize()
