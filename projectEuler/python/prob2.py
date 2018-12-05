#sum of even valued terms in fib sequence (Values under 4 million)

MAX = 4000000

	
#isEven
def is_even(input):
	if input % 2 == 0:
		return True
	else:
		return False

def next_fib_number(previous, current):
	return current + previous

def main():
	previous = 1
	current = 1
	sum = 0
	while(current < MAX):
		current = next_fib_number(previous, current)
		if is_even(current):
			sum += current
	print(sum)

main()
