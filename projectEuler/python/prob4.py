#largest palendrome made from product of 2 3 digit numbers

#make a list of all products of 2 3 digit numbers
list_of_products = []

def is_palendrome(test_value):
    reversed_string = str(test_value)[::-1]
    return True if reversed_string == str(test_value) else False

for i in range(100, 999):
    for j in range(100, 999):
        iXj = i * j
        if is_palendrome(iXj):
            list_of_products.append(iXj)

list_of_products.sort()


        
print(list_of_products)