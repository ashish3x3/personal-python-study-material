"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    else:
        return get_fib(n-1) + get_fib(n-2)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)


def getFib(position):
	if position == 0:
		return 0
	if position == 1:
		return 1
	first = 0,
	second = 1,
	next = first + second
	for i in range(position):
		first = second
		second = next
		next = first + second
	return next;