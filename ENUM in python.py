
enum in Python

import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

for Anim in (Animal):
    print(Anim)

di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

print (Animal.dog.name)
mem = Animal.dog
print (mem.name)
print (mem.value)

if Animal.dog is Animal.cat:
       print ("Dog and cat are same animals")
else : print ("Dog and cat are different animals")


from enum import Enum
Animal = Enum('Animal', 'ant bee cat dog')

or equivalently:

class Animal(Enum):
    ant = 1
    bee = 2
    cat = 3
    dog = 4

class Animal(Enum):
    DOG, CAT = range(2)


raise AttributeError

