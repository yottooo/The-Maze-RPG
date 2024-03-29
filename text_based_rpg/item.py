from collections import namedtuple

from .util import set_multiple_attributes

EQUIPPABLE = object()
CONSUMABLE = object()

class Item:
    def __init__(
            self,
            display_name,
            type_,
            effects=None,
            weight = 0

    ):
        """
        Arguments
        ---------
            display_name : str
                A readable name of the attack that can be displayed to the user.

            type_ : object
                A flag representing the type of the object; either consumable or
                equippable.

            equip_location : Optional[str]
                If the item is equippable, the equip location to equip the item
                to.

            effects : list[ItemEffect]
                The list of effects of the item when equipped or consumed.

            attacks : list[Attack]
                If the item is a weapon, the list of attacks the weapon gives
                the user.
        """
        if effects is None:
            effects = []


        set_multiple_attributes(
            self,
            display_name=display_name,
            type=type_,
            effects=effects,
            weight=weight
        )

ItemEffect = namedtuple("ItemEffect", ["stat", "modifier"])
