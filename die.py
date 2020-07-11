from random import randint 

class Die():

  def __init__(self, sides= 6): 
    self.sides = sides 

  def roll_die(self): 
    number = randint(1,self.sides)
    print(number)

  def set_number_sides (self): 
    number_sides =input("How many sides would you like? ")
    self.sides = int(number_sides)


status = 'y'
while status != 'n': 

  die = Die()
  die.set_number_sides()
  die.roll_die()
  status = input("Would you like to roll it again? y/n")

