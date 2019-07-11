from .. import interface,items
from ..util import move,pick_up
from ..room import Room

map_ = """You are at the start of the maze
To the north is the central room and the weapons and armour shop.
Goneril Mountain looms in the distance."""
items_ ="A coin is lying on the ground"

def enter(room, player):



        additional_commands = ["move"]

        command = interface.get_game_command(player, room, additional_commands)

        interface.print_multiple_lines(
            lines=[
                "Welcome to the start of your adventure hero!",
                "The re is only one way from here!",
                "Do you have what it takse to make it to the end?"
            ],
            delay=1
        )


        pick_up(player,"coin")

        place_to_move = move(["forward"])

        if place_to_move == "forward":
                room.has_been_entered_before = True
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)



room = Room(
        map_=map_,
        items_=items_,
        enter=enter
)
