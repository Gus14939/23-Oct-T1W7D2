# user input 3 numbers a b and c
a = float(input("enter #1: "))
b = int(input("enter #2: "))
c = int(input("enter #3: "))
# if a > b and a > c
    # Display a is highest
if a > b and a > c:
    print("highest number is a")
# elif a < b and b > c
    #  Display b is highest
elif a < b and b > c:
    print("highest number is b")    
# else
    # display c is highest    
else:
    print("highest number is c")
   
if a > b:
    if a > c:
        print("highest number is a")
    else:
        print("highest number is c")
else:
    if b > c:
        print("highest number is b")
    else:
        print("highest number is c")
                