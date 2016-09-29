#multiples of 3 and 5

def recCount(current, end):
	if current == end:
		return current
	else:
		return current + recCount(current + 1, end)

def recMult3and5(current, end):
	if current == end:
		if (current % 3 == 0 or current % 5 == 0):
			return current
	if (current % 5 == 0 or current % 3 == 0):
		return current + recMult3and5(current + 1, end)
	return recMult3and5(current + 1, end)
	

print recCount(1, 100)
print recMult3and5(1, 100)
