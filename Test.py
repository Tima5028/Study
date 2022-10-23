# def manyargs(*args, **kwargs):
#     print ([i**2 for i in args])
#     # print(type(args))
#     # print(args)
#     # print(kwargs)
#     # print(type(kwargs))
#
#
# result = manyargs(4, 9, 1, 3, 3, 1, var1=3, var2=6, var4=8)
# print(result)
#
# manyargs(1,2,3)


# def sum(a,b):
#     return a+b
# r=sum(1,4)
# print(r)
#
# def fibonacci(level):
#     if level in (0, 1):
#         return level
#     return fibonacci(level - 1) + fibonacci(level - 2)
# print(fibonacci(50))

# lmbd = lambda var1, var2, *args: set([var1, var2]) in set(args)
# print(lmbd(1, 2, range(5)))
# print(lmbd(8, 10, range(5)))
#
# new_lmbd = lmbd
# print(new_lmbd(8, 9, range(2)))
# print(new_lmbd(7, 6, range(100)))

# t=(lambda x,y: x+y)(5,6)
# print(t)

# [(lambda: a**2+b**3)(i) for i in range(5)](2,4)

# x={"a":17, "b":9, "c":1}
# print(x)
# print(x.keys())

# t=[i**2 for i in range(10)]
# print(t)
# print(i)

# z=a+b
# def my_func(a, b):
#     print(z)
# my_func(1, 2)

# def my_func(a, b):
#     x = 5
#     print(x)
#
# x = 10
# my_func(1, 2)
# print(x)


# def my_func(a, b):
#     global x
#     print(x)
#     x = 5
#     print(x)
#
#
# x = 10
# my_func(1, 2)
# print(x)

#
# def my_func(a, b):
#     global c
#     b, a = a, b
#     d = "Mike"
#     print(a, b, c, d)
#
#
# a, b, c, d = 1, 2, "c is global", 4
# my_func(a, b)
# print(a, b, c, d)

# def counter():
#     num = 0
#     def incrementer():
#         num += 1
#         return num
#     return incrementer
# print(counter())

# def func1(lst):
#     lst += [3]
#     return lst
#
#
# def func2(tpl):
#     tpl += (3,)
#     return tpl
#
#
# lst = [1, 2]
# tpl = (1, 2)
# print(lst)
# new_lst = func1(lst)
# new_tpl = func2(tpl)
# print("lst:", lst, "new_lst:", new_lst)
# print("tpl:", tpl, "new_tpl:", new_tpl)


# def min4():
#     a = float(input("Введите число 1: "))
#     b = float(input("Введите число 2: "))
#     c = float(input("Введите число 3: "))
#     d = float (input("Введите число 4: "))
#     return min(a,b,c,d)
#
#
# print(min4())

names=[a,b,c,d]
a,b,c,d=[float(input(f'Введите переменную ' + names [i]))for i in range(4)]

