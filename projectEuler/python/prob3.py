#largest prime factor of 600851475143

#keep a list of all factors found
list_of_factors = []
#Current number being divided
dividend = 600851475143
#Current number dividing into divisor
divisor = 2

#divide the divident by the divisor. 
#if clean division record factor, update divident
#if !clean division, increment divisor
def divide_by_input(dividend1, divisor2):
    print("here")
    if dividend1 % divisor2 == 0:
        print("in if")
        dividend = dividend1 / divisor2
        print(divisor)
        list_of_factors.append(divisor)
    else:
        print("in else")
        divisor = divisor + 1
        print(divisor)


def main():
    while divisor < (dividend/2) + 1:
        divide_by_input(dividend, divisor)
        print(list_of_factors)
        print(divisor)

main()
