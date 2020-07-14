print("write two numbers. Press 'q' to finish. \n")

while True:
  try:
    num_1 = input("Write the first number: ")
    if num_1 =='q':
      break

    x= int(num_1)
  
    num_2 = input("Write the second number: ")
    if num_2 == 'q':
      break
    
    y = int(num_2)

  except ValueError:
    print("Please enter only numbers")

  else:
    result = x + y 
    print(f"The {num_1} + {num_2} = {result}")



