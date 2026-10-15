# A piece of code that defined as a block that performs a specific action. It is defined by the "def" followed by the name of the function and ():
# the 'return' command tells python to excecute the function and also return the value. 

# def hello():
#     print("Hey this is a nice day")

# print("how is the day?")
# hello()

# def input_number():
#     return int(input("Enter a number: "))

# input1 = input_number()
# print(input1)
# input2 = input_number()
# print(input2)

#Arguments are parameters we can pass in a function. 

def input_number(num1, num2):
    return int(input("Enter a number: ")) * num2 - num1

input1 = input_number(10, 20)
print(input1)