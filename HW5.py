# 111327
# f=open(r"D:\Работа\!python\HW5\data.txt", "rt")
# sum_1=f.read().split()
# result = [int(item) for item in sum_1]
# print(sum(result))
# f.close


# 111328
# f=open(r"D:\Работа\!python\HW5\data2.txt", "rt")
# sum_1=f.read()
# sum_1=list(sum_1)
# sum_1=sum_1[::-1]
# print("".join(sum_1))
# f.close()

# 111329
# f=open(r"D:\Работа\!python\HW5\data3.txt", "rt")
# sum_1=f.read().split("\n")
# sum_1=list(sum_1)
# sum_1.reverse()
# print("\n".join(sum_1))
# f.close()

# 111335
# f=open(r"D:\Работа\!python\HW5\data4.txt", "rt")
# sum_1=f.read()
# sum_1=list(sum_1)
# a=len(sum_1)
# print(type(a))
# # b=0
# for el in range(a):
#     if  el !=" ":
#         a.append(1)
#     print(a)
# print(a)
# sum_1.reverse()
# print("\n".join(sum_1))
# f.close()


# fname = open("D:\Работа\!python\HW5\data4.txt")
# lines = 0
# words = 0
# letters = 0
# for element in fname:
#     lines += 1
#     for el in element:
#         if el==" " or el==".":
#             words+=1
#         if el!=" " and el!="." and el!="\n":
#             letters+=1
# print('Input file contains:')
# print(letters, 'Letters')
# print(words, 'Words')
# print(lines, 'lines')
# fname.close()