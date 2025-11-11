a = int(input("Enter a number:  "))
d = ""
if a == 1 :
  d = "Today is: Sunday"
elif a == 2 :
  d = "Today is: Monday"
elif a == 3 :
  d = "Today is: Tuesday"
elif a == 4 :
  d = "Today is: Wednesday"
elif a == 5:
  d = "Today is: Thursday"
elif a == 6:
  d = "Today is: Friday"
elif a == 7 :
  d = "Today is: Saturday"
else :
  print("Invalid day number.")
  breakpoint

print(d)
