"""This module contains code for the main command loop of the game."""

from .get_command import get_command
from .print_multiple_lines import print_multiple_lines
from .built_in_methods import print_

_MAP = "map"
_STATS = "stats"
_INVENTORY = "inventory"
_CONSUME_ITEM = "use item"
_PICKUP_ITEM = "pick up item"
_DISCARD_ITEM = "discard item"
_SEARCH_ITEMS = "look for items"

_BASE_COMMANDS = [
    _MAP,
    _STATS,
    _INVENTORY,
    _CONSUME_ITEM,
    _SEARCH_ITEMS,
    _DISCARD_ITEM
]

def get_game_command(player, room, additional_commands=[]):
    """
    Get a general game command from the player and execute it.

    Arguments
    ---------
        player : Player
            The player.

        room : Room
            The room the player is currently in.

        additional_commands : Optional[list]
            A list of additional commands to allow the play to enter.

    Returns
    -------
    None

    """
    commands = additional_commands.copy()
    commands.extend(_BASE_COMMANDS)

    while True:
        print_()
        command = get_command(commands, True)

        if command in additional_commands:
            return command

        if command == _MAP:
            print_multiple_lines(room.map.split("\n"), 1)

        if command == _STATS:
            player.stats_view()

        if command == _INVENTORY:
            player.inventory_view()

        if command == _CONSUME_ITEM:
            player.use_item_interface()

        if command == _DISCARD_ITEM:
            player.discard_item_interface()

        if command == _SEARCH_ITEMS:
            print_multiple_lines(room.items.split("\n"), 1)

