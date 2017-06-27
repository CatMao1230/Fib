def fib():
	a = 1
	b = 2
	yield a
	yield b
	while 1:
		c = a + b
		a = b
		b = c
		yield c

c = fib()
print c.next()
print c.next()
print c.next()
print c.next()
print c.next()