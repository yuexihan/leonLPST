from leonLPST import LPSTree
import random
from six.moves import xrange

N = 1*10**6
LOOP = 1000
MOD = 10**3 + 7

random.seed(1)
l1 = LPSTree(N)
result1 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		l1.add(x, y, diff)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		l1.set(x, y, value)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result1.append(l1.get(x, y))

random.seed(1)
l2 = [0] * N
result2 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] += diff

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] = value

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result2.append(sum(l2[x:y]))

# print result1
# print result2
assert result1 == result2
assert l1.tolist() == l2

#######################################
random.seed(1)
l1 = LPSTree(N, reducef=max)
result1 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		l1.add(x, y, diff)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		l1.set(x, y, value)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result1.append(l1.get(x, y))

random.seed(1)
l2 = [0] * N
result2 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] += diff

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] = value

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result2.append(max(l2[x:y]))

# print result1
# print result2
assert result1 == result2
assert l1.tolist() == l2

#######################################

random.seed(1)
l1 = LPSTree(N, modulo=MOD)
result1 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		l1.add(x, y, diff)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		l1.set(x, y, value)

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result1.append(l1.get(x, y))

random.seed(1)
l2 = [0] * N
result2 = []
for i in xrange(LOOP):
	if i%100 == 0:
		print i
	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	diff = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] += diff
			l2[i] %= MOD

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	value = random.randint(0, N)
	if random.randint(0, 1):
		for i in xrange(x, y):
			l2[i] = value
			l2[i] %= MOD

	x = random.randint(0, N)
	y = random.randint(0, N)
	if x == y:
		continue
	if x > y:
		x, y = y, x
	if random.randint(0, 1):
		result2.append(sum(l2[x:y])%MOD)

# print result1
# print result2
assert result1 == result2
assert l1.tolist() == l2
