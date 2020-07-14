print("write two numbers. Press 'q' to finish. \n")

while True:
  num_1 = input("Write the first number: ")
  if num_1 =='q':
    break
  
  num_2 = input("Write the second number: ")
  if num_2 == 'q':
    break

  try:
    result = int(num_1 ) + int(num_2)
  except ValueError:
    print("Please enter only numbers")
  else:
    print(f"The {num_1} + {num_2} = {result}")

