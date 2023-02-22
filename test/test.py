l = [5, 3, 8, 2, 1, 4, 2, 4, 11, 5]
k = 11
for i in range(len(l)):
    o = ''
    e = 0
    for j in range(i, len(l)):
        e += l[j]
        o = o+str(l[j])+','
        if e == k:
            o = o.removesuffix(o[len(o)-1])
            print(o)
        elif e > k:
            break


# l=['right','right','right','left','right','right','left','left','left','right','left','left','right']
# c=0
# count=0

# for i in l:
#     if i=='right':
#         c=c+90
#         if c==360:
#             count=count+1
#             c=0
#     else:
#         c=c-90
#     if i=='left':
#         angle=
#         c=c-90
#         if c==0:
#             count=count+1
#             c=0
#     else:
#         c=c-90

# print(count)


s='baccbbbdabcdbca'
n='abc'
l=[]
data = ['abc','acb','bac','bca','cab','cba']
for i in range(len(s)-2):
    if s[i:i+3] in data:
        l.append(i)
print(l)
