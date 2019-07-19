def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print "Fibonacci using next function"
x = fib(5)
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()

print "Fibonacci using for-in loop"
for i in fib(5):
    print i

# Difference between range and x-range
a = range(1, 5)
print a

a = xrange(1, 5)
print a
for j in xrange(1, 5):
    print j
