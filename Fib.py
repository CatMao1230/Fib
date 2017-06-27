def fib():
	a = 1
	b = 1
	yield a
	while True:
		a, b = b, a + b
		yield b

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()