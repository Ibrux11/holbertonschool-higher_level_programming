# task_05_dragon.py

class SwimMixin:
	def swim(self):
		print("The creature swims!")

class FlyMixin:
	def fly(self):
		print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
	def roar(self):
		print("The dragon roars!")

# main_05_dragon.py

#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!