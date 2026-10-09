x = 3
guess = int(input('guess the number:'))
while guess != x:
    guess = int(input('guess the number:'))
    print("The number is wrong")
else:
    print("The number is right")