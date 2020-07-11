filename = 'guest.txt'

while True:
  name = input("What's your name? (Enter 'q' to finish) ")
  if name == 'q':
    break
  else:
    with open(filename, 'a') as f: 
      f.write(name.title() + "\n")
      print(f"Welcome {name}")



