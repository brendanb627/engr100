from errors import SandwichException

BREAD_NAME = "Slice of Bread"
PB_NAME = "Peanut Butter"
JELLY_NAME = "Jelly"

class Container:
    def __init__(self, name):
        self.opened = False
        self.knife = None
        self.name = name
    def open(self):
        if self.opened == True:
            raise SandwichException(f"{self.name} is already open. Cannot be opened again.")
        else:
            print (f"Opened {self.name}")
            self.opened = True
    def close(self):
        if self.opened == False:
            raise SandwichException(f"{self.name} is already closed. Cannot be closed again.")
        elif self.knife:
            raise SandwichException(f"You can't close {self.name} because there is a knife in it!")
        else:
            print (f"Closed {self.name}")
            self.opened = False



class BreadBag(Container):
    def __init__(self):
        super().__init__("Bread Bag")
        self.contains = [Bread() for x in range(10)]
    def take_out(self, num):
        if self.opened == False:
            raise SandwichException("Can't take bread from closed bag!")
        if len(self.contains) - num < 0:
            raise SandwichException(f"Bread bag only has {len(self.contains)} slices. Can't take out {num}")
        else:
            return_slices = self.contains[-num:]
            self.contains = self.contains[:-num]
            print(f"Took {num} slices of bread out. {len(self.contains)} remaining.")
            return return_slices
        

class Bread:
    def __init__(self):
        self.name = BREAD_NAME
        self.contains = None

class JellyJar(Container):
    def __init__(self):
        super().__init__("Jelly Jar")
        self.contains = Jelly()

class Jelly:
    def __init__(self):
        self.name = JELLY_NAME

class PBJar(Container):
    def __init__(self):

        super().__init__("Peanut Butter Jar")
        self.contains = PB()

class PB:
    def __init__(self):
        self.name = PB_NAME

class Knife:
    def __init__(self):
        self.contains = None
        self.inside = None
    def scoop(self):
        if (not self.inside):
            raise SandwichException("Knife can't scoop anything because it's not inside of anything.")
        elif self.contains:
            raise SandwichException(f"Knife cannot scoop because it already contains {self.contains.name}.")
        else:
            self.contains = self.inside.contains
            print(f"Knife now contains {self.contains.name}")
            
    def insert(self, obj):
        if self.inside:
            raise SandwichException(f"Knife is already inside of {self.inside.name}")
        else:
            if not obj.opened:
                raise SandwichException(f"Can't insert knife into {obj.name} because it is not open.")
            self.inside = obj
            self.inside.knife = self
            print(f"Inserted knife into {self.inside.name}.")

    def remove(self):
        if not self.inside:
            raise SandwichException("Knife is currently not inside of anything.")
        else:
            self.inside.knife = None
            self.inside = None
    def spread(self, bread):
        if self.inside:
            raise SandwichException(f"Can't spread contents because knife is currently inside of {self.inside.name}.")
        if bread.name != BREAD_NAME:
            raise SandwichException(f"{bread.name} is not a slice of bread!")
        elif not self.contains:
            raise SandwichException("Knife does not have anything on it.")
        else:
            bread.contains = self.contains
            self.contains = None
            print(f"{bread.name} now contains {bread.contains.name}. Knife is now empty.")


class Sandwich():
    def __init__(self, slice_1, slice_2):
        self.slice_1 = slice_1
        self.slice_2 = slice_2

    def validate(self):
        if (not self.slice_1.contains and not self.slice_2.contains):
            raise SandwichException("Both slices of bread are empty.")
        if (not self.slice_1.contains):
            raise SandwichException("Slice 1 doesn't have anything on it")
        if (not self.slice_2.contains):
            raise SandwichException("Slice 2 doesn't have anything on it")
        if self.slice_1.contains.name == PB_NAME and self.slice_2.contains.name == JELLY_NAME or self.slice_1.contains.name == JELLY_NAME and self.slice_2.contains.name == PB_NAME:
            return True
        else:
            return False