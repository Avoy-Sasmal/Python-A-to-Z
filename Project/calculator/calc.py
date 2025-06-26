def add(x,y) :
  return x+ y

def subtract(x,y) :
  return x - y

def multiply(x,y) :
  return x * y

def divide(x,y) :
  if(y==0):
    return "Cannot divide by zero"
  else:
    return x / y 
  
print("Welcome to the calculator program")  
print("please Enter the Two Numbers ")
  
x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))  

while(1):
  print("enter your choice \n 1. Add two numbers \n 2. Subtract two numbers \n 3. Multiply two numbers \n 4. Divide two numbers")
  choice = input("Enter choice(1/2/3/4): ")
  if(choice == '1'):
      print("You chose to add two numbers",add(x, y))
  elif(choice == '2'):
      print("You chose to subtract two numbers", subtract(x, y))  
  elif(choice == '3'):
      print("You chose to multiply two numbers", multiply(x, y))
  elif(choice == '4'):
      print("You chose to divide two numbers", divide(x, y))
  else:  
     break
print("Exiting the calculator program")  

