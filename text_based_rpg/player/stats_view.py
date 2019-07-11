from .. import interface


def _print_line(player):
    """
    Print a line of the view displaying the player's stats.

    Arguments
    ---------
        player : Player
            The player.

        value_name : str
            The name of the stat to print the line for.
    """
    interface.print_("Your Health is "+player.health)


def stats_view(player):
    """
    Display a list of the items the player's stats.

    Arguments
    ---------
        player : Player
            The player.

    Returns
    -------
    None

    """

    interface.print_("Your Health is "+player.health)


