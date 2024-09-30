from ingredients import Sandwich
from errors import SandwichException


def assemble(slice_1, slice_2):
    sandwich = Sandwich(slice_1, slice_2)
    return sandwich

def validate(sandwich, bread_bag, pb_jar, jelly_jar, knife):
    if not sandwich:
        raise SandwichException(f"You didn't make a sandwich yet!")
    if not sandwich.validate():
        raise SandwichException(f"Bread slices do not contain correct ingredients. Slice 1 contains {sandwich.slice_1.contains.name} and Slice 2 contains {sandwich.slice_2.contains.name}")
    for i in [bread_bag, pb_jar, jelly_jar]:
        if i.opened:
            raise SandwichException(f"You forgot to close {i.name}")
    if knife.contains:
        raise SandwichException(f"Knife isn't clean. It contains {knife.contains.name}")
    print("Congratulations! You made a peanut butter and jelly sandwich! Enjoy!")
    
    


