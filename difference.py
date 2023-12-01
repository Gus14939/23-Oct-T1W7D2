# x = get first 100 numbers
x = []
for i in range (1, 101):
    x.append(i)

# a = square each number
a = sum(i ** 2 for i in x)
# a = add all numbers

# b_y = add all numbers
b_y = sum(x)
# b = square b_y
b = b_y ** 2
# output q = b - a
# q = b - a
print(b - a)

#while loop <= 100
#define the sum_of_squares
#define the square_of_sum
# i = 1

sum_of_squares = 0
square_of_sum = 0
i = 1
while i <= 100:
    sum_of_squares = (i**2) + sum_of_squares
    square_of_sum = i + square_of_sum
    i = i + 1
square_of_sum = square_of_sum ** 2
print(square_of_sum - sum_of_squares)


sum_of_squares = 0
square_of_sum = 0
for i in range(1, 101):
    sum_of_squares += (i**2)# + sum_of_squares
    square_of_sum += i # + square_of_sum
square_of_sum = square_of_sum ** 2
print(square_of_sum - sum_of_squares)