#Python program
#largest prime factor of 600851475143

def main():
    initial_value = 600851475143
    #keep a list of all factors found
    list_of_factors = []
    #Current number being divided
    dividend = 600851475143
    #Current number dividing into divisor
    divisor = 2
    
    while divisor < (initial_value/2) + 1:
        print(divisor)
        calculated = divide_by_input(dividend, divisor)
        if calculated == -1:
                divisor = divisor + 1
        else:
                dividend = calculated
                list_of_factors.append(divisor)
    print(list_of_factors)


#divide the divident by the divisor. 
#if clean division record factor, update divident
#if !clean division, increment divisor
def divide_by_input(dividend, divisor):
    return_value = 0
    if dividend % divisor == 0:
        return_value = dividend / divisor
    else:
        return_value = -1
    return return_value

main()
