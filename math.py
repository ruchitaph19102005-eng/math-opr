try :
  a = float(input("Enter first number:"))
  b = float(input("Enter first number:"))
  print(f"Addition:{a +  b}")
  print(f"Subtraction:{a - b}")
  print(f"Multiplication:{a * b}")
  if b !=0:
        print(f"Division:{a / b}")
  else:
        print("Division by zero is not allowed.")
except valueerror:
  print("Please enter valid numbers.")
  
