from . import consume, inventory_view, \
    use_item_interface, inventory_properties, \
    stats_view, discard_item_interface


class Player:
    def __init__(self, name):
        self.health = 3
        self.inventory = []
        self.name = name


    consumable_items = inventory_properties.consumable_items


    consume = consume.consume


    inventory_view = inventory_view.inventory_view
    stats_view = stats_view.stats_view
    use_item_interface = use_item_interface.use_item_interface
    discard_item_interface = discard_item_interface.discard_item_interface
   # pick_up_item_interface = pick_up_item_interface.pick_up_item_interface

