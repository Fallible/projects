#Difference between sumOfSquare squareOfSum 100
import math

sum_of_square = 0
square_of_sum = 0

for i in range (1,100):
    sum_of_square = sum_of_square + pow(i, 2)
    square_of_sum = square_of_sum + i

print(sum_of_square)
print(square_of_sum)
print(sum_of_square - square_of_sum)