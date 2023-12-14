def my_fun( *kids):
    print("good kidss:" +kids[2])
my_fun("hema","hari","latha")    
def my_func(c1,c2,c3):
    print("youngest child:"+c2)
my_func(c1="abhi",c2="ram",c3="reddy")
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
def my_funct(x):
  return 5 * x

print(my_funct(3))
print(my_funct(5))

def add(num1: int, num2: int) -> int:
   
    num3 = num1 + num2
 
    return num3
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)