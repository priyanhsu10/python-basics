import random
import secrets

a = random.random()
b = random.uniform(1, 10)
c = random.randint(1, 10)
d = random.normalvariate(0, 1)
print(d)

mylist = list('asdfasdfv3e4r34')
e = random.choice(mylist)
random.shuffle(mylist)


random.seed(1)
print(random.random())

sr = secrets.randbelow(10)
sb = secrets.randbits(6)
print(sb)
