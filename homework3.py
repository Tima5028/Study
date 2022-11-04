# 334
# names=[]
# names=[float((input('Введите переменную ')))for i in range(4)]
# for e in names:
#     if e%names[3]!=0:
#         print(round(e,0))
# else:
#     print("")

# 3642
# N=int(input("Введите число: "))
# for i in range(10):
#     if i**2<N and i**2!=0:
#         print(i**2)


# 3644
# N=int(input("Введите число: "))
# for i in range(100):
#     if 2**i<N and i**2!=0:
#         print(2**i)

# 3647
# X=int(input("Введите количество киллометров в первый день: "))
# Y=int(input("Введите количество желаемых киллометров: "))
# Z=0
# while Y-X>0:
#     X*=1.1
#     Z+=1
# print(Z)

# 3533
# n=int(input("Введите число: "))
# x=1
# for i in range (1,n+1): x=x*i
# print(x)

# 3535
# n=int(input("Введите число пингвинов: "))
# # for i in range (1,n+1):
# print("    _~_   "*n,"\n","  (o o)   "*n,"\n", " /  V  \  "*n,"\n","/(  _  )\ "*n,"\n","  ^^ ^^   "*n)

# 3535_2
peng = [
  '   _~_    ',
  '  (o o)   ',
  ' /  V  \\  ',
  '/(  _  )\\ ',
  '  ^^ ^^   '
]

request = int(input("Enter number of ping:"))
for i in peng: print(request * i)

# # 3791
#
# def dist():
#     a = float(input("Введите x1: "))
#     b = float(input("Введите y1: "))
#     c = float(input("Введите x2: "))
#     d = float (input("Введите y2: "))
#     r=(((c-a)**2)+((d-b)**2))**(1/2)
#     return r
# print(dist())


# 3795
# def IsPointInFirst(x, y):
#     inCircle = (x + 1) ** 2 + (y - 1) ** 2 <= 4
#     aboveFirstLine = x + y >= 0
#     aboveSecondLine = y - 2 * x - 2 >= 0
#     return inCircle and aboveFirstLine and aboveSecondLine
#
# def IsPointInSecond(x, y):
#     outCircle = (x + 1) ** 2 + (y - 1) ** 2 >= 4
#     underFirstLine = x + y <= 0
#     underSecondLine = y - 2 * x - 2 <= 0
#     return outCircle and underFirstLine and underSecondLine
#
# def IsPointInArea(x, y):
#     return IsPointInFirst(x, y) or IsPointInSecond(x, y)
#
# x, y = float(input()), float(input())
# if IsPointInArea(x, y):
#     print('YES')
# else:
#     print('NO')

# calc
# y=['-','+','*','^','/']
# z=1
# while z==1:
#     x=(str(input("Введите вырвжение: ")))
#     if x=="stop" or x=="Stop" or x=="STOP":
#         print("Good bye")
#         break
#     x=list(x)
#     a = int(x[0])
#     b = int(x[2])
#     if y in x:
#         x.split(y)
#         x[1]=str(x[1])
#     if x[1]=="+":
#         print("Ответ: ",a+b)
#     elif x[1]=="-":
#         print("Ответ: ",a-b)
#     elif x[1] == "*":
#         print("Ответ: ",a * b)
#     elif x[1] == "^":
#         print("Ответ: ",a ** b)
#     elif x[1] == "/":
#         print("Ответ: ",a /b)
#
