"""Variables"""
my_example = "hello world" # let myExample = "hello world"
MY_EXAMPLE = "hello world" # const myExample = "hello world" (mutable, but make it upper case as signal not to overwrite)


"""Lists and Arrays"""
# arrays are called "lists" in Python
my_list = [1,2,3] # const myList = [1,2,3]


"""Functions"""
def foo(str):
    print(str)
# const foo = (str) => console.log(str)


"""If Statements"""
def foo(num):
    if num == 1:
        print("number 1")
    elif num == 2:
        print("number 2")
    else:
        print("random number")


"""Conditionals"""
def foo(condition1, condition2):
   if condition1 == 1 or condition2 == 2:
      print("hey")
   elif condition1 == 1 and condition2 == 2:
    print("hey hey")
   elif not condition1:
    print("howdey") 

# and <=> &&
# or <=> ||
# not <=> !


"""For Loops"""
def showNum(num):
    for i in range(num):
        print(i)
# for(let i = 0; i < num; i++) {
# console.log(i)
# }

