# - Data Types
## - Numbers
num1 = 42
## float
num2 = 2.3
## Boolean
boolean = True
## Strings
string = 'Hello World'
## List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
## Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
## Tuples
fruit = ('blueberry', 'strawberry', 'banana')
## type check
print(type(fruit))
## list - access value
print(pizza_toppings[1])
## add value
pizza_toppings.append('Mushrooms')
## access value
print(person['name'])
## add value
person['name'] = 'George'
person['eye_color'] = 'blue'
## access value
print(fruit[2])
# conditionals
## if/else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
## if/elseif/else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# for loops
## start at o end at 4
for x in range(5):
    print(x)
## start at 2 and 4
for x in range(2,5):
    print(x)
## increment by 3
for x in range(2,10,3):
    print(x)
# while loop
x = 0
while(x < 5):
    print(x)
    x += 1
## list delete value
pizza_toppings.pop()
pizza_toppings.pop(1)
## log statement
print(person)
### list delete value
person.pop('eye_color')
print(person)
##conditional
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
## function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
## function 
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
## function 
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)