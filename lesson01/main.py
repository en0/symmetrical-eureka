from .linked_list import LinkedList
from . import fake_data


def move_player(d):
    if d is not None:
        print(f"  Player is moving {d}")


ll = LinkedList()
for action, direction in fake_data.input_keys:
    print(f"+ {direction} was {action}")
    if action == fake_data.PRESSED:
        ll.add(direction)
    elif action == fake_data.RELEASED:
        ll.remove(direction)
    else:
        pass

    current_direction = ll.peek()
    if current_direction:
        move_player(current_direction)

