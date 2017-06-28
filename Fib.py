def fib():
	a = 0
	b = 1
	while True:
		a, b = b, a + b
		yield b

if __name__ == '__main__':
	c = fib()
	print c.next()
	print c.next()
	print c.next()
	print c.next()
	print c.next()