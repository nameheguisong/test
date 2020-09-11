# alist=[{"name":"a", "age":20}, {"name":"b", "age":30}, {"name":"c", "age":25}]
# b = []
# for a in alist:
#     b.append(a['age'])
# #
# # c = [b.append(i['age']) for i in alist]
# print(sorted(b))
#
#
# # 直接改变b里面的排序值
# b.sort(reverse=True)
# print(b)
# from collections import Counter
# a=['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']
#
# # b = a.count('apple')
#
# b = Counter(a)
# print(b)
# a = 1
# def fun(a):
#   a = 2
# fun(a)

a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3, 4, 5]

for j,k in zip(a,b):
    l = {'{}:{}'.format(j,k)}
    print(l)