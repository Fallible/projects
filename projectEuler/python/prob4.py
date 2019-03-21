#largest palendrome made from product of 2 3 digit numbers

#make a list of all products of 2 3 digit numbers
list_of_products = []

for i in range(100, 999):
    for j in range(100, 999):
        iXj = i * j
        if iXj > 900000:
            list_of_products.append(iXj)

list_of_products.sort()

def is_palendrome()
        
print(list_of_products)