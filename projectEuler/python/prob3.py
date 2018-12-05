#largest prime factor of 600851475143

list_of_factors = []
dividend = 600851475143
divisor = 2

def divide_by_input(dividend, divisor):
    result = 0
    while dividend % divisor != 0:
        result = dividend / divisor
    return result

def main():
    while divisor < dividend:
        list_of_factors.append(divide_by_input(dividend, divisor))
        print(list_of_factors)

main()
