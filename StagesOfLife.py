#Stages of life 

age= 20

if age < 0:
  person = ("Are you planning to start a family?")
elif age < 2:
  person = 'baby'
elif age == 2 or  age < 4:
  person = 'toddler'
elif age == 4 or age < 13:
  person = 'kid'
elif age == 13 or age < 20: 
  person = 'teenager'
elif age == 20 or age < 65: 
  person = 'adult'
elif age >= 65:
  person = 'elder'

print("You are a/an " + person)