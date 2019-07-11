"""This modules contains the code representing the items in the game."""

from . import item

#coin = item.Item(
#    display_name="a coin lying on the ground",
#    type_=item.EQUIPPABLE,
#    weight = 1
#)


def health_potion():
    return item.Item(
        display_name="Health potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="health", modifier=10)]
    )

def stamina_potion():
    return item.Item(
        display_name="Stamina potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="stamina", modifier=10)]
    )

def mana_potion():
    return item.Item(
        display_name="Mana potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="mana", modifier=10)]
    )
