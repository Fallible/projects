#multiples of 3 and 5

def rec_count(current, end):
	if current == end:
		return current
	else:
		return current + rec_count(current + 1, end)

def rec_mult_3and5(current, end):
	if current == end:
		if (current % 3 == 0 or current % 5 == 0):
			return current
	if (current % 5 == 0 or current % 3 == 0):
		return current + rec_mult_3and5(current + 1, end)
	return rec_mult_3and5(current + 1, end)
	

print(rec_count(1, 100))
print(rec_mult_3and5(1, 100))
