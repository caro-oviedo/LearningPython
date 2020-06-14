#Slices 

dogs = ['Pepa', 'Canela', 'Broccoli', 'Almendra', 'Escopeta', 'Pochoclo']
print("The first three dogs in my list are:")
for dog in dogs[:3]:
  print(dog.title())

print("Three items form the middle of the list are: ")
middle= len(dogs) / 2
mid =(int(middle))
test= middle + 3
test= int(test)

for dog in dogs[mid:test]: 
  print(dog)



print("The last three items in the list are:")
for dog in dogs[-3:]:
  print(dog.title())

my_pizzas = ['Pepperoni', 'Margherita', 'Napolitan','Mushroom', 'Marinara', 'Hawaiian']

friend_pizzas = my_pizzas[:]

my_pizzas.append('Seafood')
friend_pizzas.append('Onion')

print("My favourite pizzas are: ")
for pizza in my_pizzas: 
  print(pizza)

print ("My friend's favourite pizzas are: ")
for pizzaf in friend_pizzas: 
  print(pizzaf)



