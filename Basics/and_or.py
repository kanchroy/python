age1 = int(input("what is your age: "))
age2 = int(input("what is your age: "))
if (age1 >= 18 and age2 >= 18):
   print("You are both adults")
elif(age1 >= 18 or age2 >= 18):
   print("One of you is an adult")
else:
   print("None of you are adults")