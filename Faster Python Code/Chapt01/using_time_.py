from time import perf_counter


def upto_for(n):
	total = 0
	for i in range(n):
		total += i
	return total

def upto_sum(n):
	return sum(range(n))

def upto_compre(n):
	return sum([val for val in range(n)])


if __name__=='__main__':
	n = 1_000_000

	start = perf_counter()
	upto_for(n)
	duration = perf_counter() - start
	print('upto_for', duration)

	start = perf_counter()
	upto_sum(n)
	duration = perf_counter() - start
	print('upto_sum', duration)

	start = perf_counter()
	upto_compre(n)
	duration = perf_counter() - start
	print('upto_compre', duration)


