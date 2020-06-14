glossary = {
  'table': 'piece of wood with four legs',
  'chair': 'piece of wood used to sit on ',
  'cofee maker': 'machine used to make coffee',
}

for word,definition in glossary.items():
  print (word)
  print (definition.title() + "\n")

rivers ={ 
  'Amazon': 'Peru',
  'Ob': 'Russia',
  'Mississippi': 'United States',
}

for name in rivers.keys(): 
  print(name.title() + " runs through " 
    + rivers[name])

print("\nList of rivers: \n")

for river in rivers.keys(): 
  print(river)

print("\nList of countries: \n")

for country in rivers.values():
  print(country)
