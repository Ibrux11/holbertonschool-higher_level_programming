# task_04_flyingfish.py

class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# main_04_flyingfish.py

#!/usr/bin/env python3
from task_04_flyingfish import FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()    # Outputs: The flying fish is swimming!
flying_fish.fly()     # Outputs: The flying fish is soaring!
flying_fish.habitat() # Outputs: The flying fish lives both in water and the sky!

# Exploring Method Resolution Order (MRO)
print(FlyingFish.mro())