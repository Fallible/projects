import math
#Smallest positive number evenly divisible by all numbers 1 to 20

list_of_primes = []
current_sum = 1

def is_prime (num_to_check):
    for i in range(2, num_to_check):
        if num_to_check % i == 0:
            return False
    return True

for q in range(1, 21):
    if(is_prime(q)):
        list_of_primes.append(q)

for p in list_of_primes:
    current_sum = current_sum * p

print(current_sum)






