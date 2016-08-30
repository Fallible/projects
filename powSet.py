# Outputs the powerset of a given set

def powSet(sourceList, resultList):
	if len(sourceList) == 0:
		return [resultList]
	else:
		item = sourceList[0]
		remainder = sourceList[1:]

		resultA = powSet(remainder, resultList)
		resultB = powSet(remainder, resultList.append(item))
		return resultA + resultB

def doAll(sourceList, foo, resultList = []):
	if len(sourceList) == 0:
		return [foo(resultList)]
	else:
		item = sourceList[0]
		remainder = sourceList[1:]

		resultA = doAll(list(remainder), foo, list(resultList))
		resultList.append(item)
		resultB = doAll(list(remainder), foo, list(resultList))
		return resultA + resultB


def myFunc(someList):
	print(someList)
	return len(someList)

print(doAll([1, 2, 'B'], myFunc))

