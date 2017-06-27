def fib():
	a = 1
	b = 2
	yield a
	yield b
	while 1:
		a, b = b, a + b
		yield b

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()