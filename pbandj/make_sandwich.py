# Goal: Let's try to make a PB&J Sandwich
# We need to give instructions to successfully complete the sandwich
from functions import *
from ingredients import BreadBag, PBJar, JellyJar, Knife

bread_bag = BreadBag()
# BreadBag contains the following functions: 
#   open(), 
#   close(), 
#   take_out(num) [num is number of slices of bread to take out] -> returns the slices of bread


pb_jar = PBJar()
# PBJar contains the following functions: 
#   open(), 
#   close() 


jelly_jar = JellyJar()
# JellyJar contains the following functions: 
#   open(), 
#   close()


knife = Knife()
# Knife contains the following functions:
#   insert(obj) [obj is the object the knife is being inserted into]
#   remove() knife is removed from whatever object it is inside
#   scoop() knife scoops the contents of whatever object it is inside of.
#   spread(bread) [bread is a slice of bread], spreads the contents of the knife onto the bread. This leaves the knife clean.

# once your bread is ready, you can use assemble(slice_1, slice_2) to put the slices together.




# instructions

# create your instructions here






# replace with the assembled sandwich
sandwich = None
# sandwich = assemble(slice_1, slice_2)

# validate everything
validate(sandwich, bread_bag, pb_jar, jelly_jar, knife)




