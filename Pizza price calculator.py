print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
if size == "S":
  bill = 15
  print("Small Pizza costs $15")
elif size == "M":
  bill = 20
  print("Medium Pizza costs $20")
else:
  bill = 25
  print("Large Pizza costs $25")

add_pepperoni = input("Do you want pepperoni? Y or N \n")
if add_pepperoni == "Y":
  if size == "S":
   bill += 2
  else:
   bill += 3

extra_cheese = input("Do you want extra cheese? Y or N \n")
if extra_cheese == "Y":
  bill += 1

print(f"Your total bill is ${bill}.")





