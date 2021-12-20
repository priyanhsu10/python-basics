# message = "hello"
# print(len(message))

# print(message.capitalize())
# print(message.count('ll'))

# print(message.replace("l","x"))

# num=2.4
# s="test"
# print(type(s))
# print(type(num))
# print(3%2)
# couase=[12,2,4,5,6,10]
# test=[1,1,1]
# couase.append(100)
# couase.insert(1,300)
# couase.extend(test)
# print(couase)
# couase.reverse();
# couase.sort(reverse=True)
# print(sorted(couase))
# print(couase)
# print(min(couase))
# print(max(couase))
# print(sum(couase))
# print(sum(couase)/len(couase))

# for  index , item in enumerate(couase,start=1):
#       print(f"{item} :{index}")

# newcassue =["maths","science","marathi","engilsh"]
# # couase_str= ':'.join(newcassue)

# # print(couase_str.split(':'))
# # print(couase_str)

# newtuple= ("maths","science","marathi","engilsh")
# # print(newtuple)

# setcource={"maths",'physics','computer','english'}
# set2= {"maths","science","marathi","english"}

# print(setcource.union(set2))

# emptylist=[]
# emtyset=set()
# emtydic={}
# print(type(emptylist))
# print(type(emtyset))
# print(type(emtydic))

# student ={'name':'jon', 'age':29,'courses':['maths','science']}
# # student['phone']= 23409237
# student.update({'phone':2349023874})
# print(student.get('courses','not_found'))
# print(student.get('phone'))
# print(student)

# # del student['age']
# age= student.pop( "age")
# print(age)
# print(student)
# print(student.values())
# print(student.keys())

# a=[1,2,3]
# b=[1,2,3]
# print (id(a))
# print(id(b))
# if a==b:
#     print('equal')

# if a is b:
#     print('true')
# else:
#     print('false')
# count =0
# while True:
#   count+=1
#   print(count)
#   if count==10:
#       break

# from timeit import default_timer as timer


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# student_info('maths', 'Art', name='sam', sirname='lue')

# set1 = set()
# set1.add(1)
# set1.add(3)
# set1.add(1)
# print(set('hello'))
# start = timer()
# for index, i in enumerate('hello', start=1):
#     print(f'{i} : {index}')
# stop = timer()
# print(stop-start)
# list = ['b'*3]*3
# print(list)

from collections import Counter

# stringvar = "aaaabbbeeeeessscssssdws"
# c = Counter(stringvar)
# print(list(c.elements()))


# def mult(x, y): return x*y


# print(mult(10, 10))

# points = [(1, 2), (15, -1), (5, -1), (10, 1)]

# poits_sorted = sorted(points, key=lambda x: x[0]+x[1])
# print(points)
# print(poits_sorted)
from functools import reduce
a = [1, 23, 4, 5, 6, 7, 6]
b = map(lambda x: x*2, a)
# print(list(b))
# c = [x*2 for x in a]
# print(c)

# b = filter(lambda x: x % 2 == 0, a)

# print(list(b))
# c = [x for x in a if x % 2 == 0]
# print(c)
# product_a = reduce(lambda x, y: x*y, a)
# print(product_a)

# # -----------------exception

# # f = open("hello.py")
# # print(f.readlines())
# try:
#     a = 5 + "10"
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     print('clean up')


# class valueToHighError(Exception):
#     pass


# def test_value(v):
#     if v > 100:
#         raise valueToHighError('value to high')


# test_value(200)
