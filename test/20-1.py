# n = 4
# for j in range(50):
#     if j>1:
#         flag=True
#         for i in range(j):
#             if i>1:
#                 if j%i!=0:
#                     continue
#                 else:
#                     flag=False
#                     break
#         if flag:
#             print('no is prime,  ',j)
        
# n=10011
# temp = n
# rev_no = 0
# while n>0:
#     digit = n%10
#     rev_no=rev_no*10 + digit
#     n=n//10
# if temp==rev_no:
#     print('no is palindrome')
# else:
#     print('no is not palindrome')
    
    
# s= 'abhayahba'
# ns=s[::-1]

# l=[]
# for i in s:
#     l.append(i)
# l.reverse()
# ns=''.join(l)  
# if ns==s:
    # print('str is palindrome')
# else:
    # print('str is not palindrome')

# ns=''
# for i in range(-1,-len(s),-1):  
#         ns=ns+s[i]
# print('str is palindrome') if s==ns else print('str is not palindrome')



# def fact(a):
#     if 0<a<2:
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(3))

# n=6
# facto=1
# while n>1:
#     facto=facto*n
#     n=n-1
# print(facto)



# n=153
# strong=0
# while n>0:
#     digit=n%10
#     strong=strong +fact(digit)
#     n=n//10
# if n==strong:
#     print('strong no')
# else:
#     print('strong no')


# def fibgen(n):
#     a,b=0,1    
#     for i in range(n):
#         yield a
#         c=a
#         a=b
#         b=a+c      
       
# for x in fibgen(10):
#     print(x)



# s= 'i am  indian'
# d={}
# for i in s:
#     if i.isalpha():
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]=d[i]+1
# print(d)


# a = int (input('enter number : - '))
# for i in range(1,a+1):
#     d={i:i**2}
#     print(d)


# l=[]
# for i in range(10):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             l.append(i)
# print(l)


# s='abhayahba'
# ns=''
# n=len(s)
# while n>0:
#     ns=ns+s[n-1]
#     n=n-1
# if s==ns:
#     print('str is pallindrome')
# else:
#     print('str is not pallindrome')
    
# n=10
# a = 0
# b=1
# print(a)
# for i in range(n-1):
#     print(b)
#     c=a
#     a=b
#     b=c+a

# n=60
# a,b=0,1
# print(a)
# while b<=n:
#     print(b)
#     c=a
#     a=b
#     b=c+a

# def fib(a):
#     if a<=1:
#         return a
#     else:
#         return fib(a-1)+fib(a-2)

# n=10
# if n<=0:
#     print('invalid')
# else:
#     for i in range(n):
#         print(fib(i))


# s='sscccddaaeeffg'
# ch=''
# c=1
# o=''
# for i in range(len(s)):
#     if s[i] not in ch:
#         o=o+ch+str(c)
#         c=1
#         ch=s[i]
#     else:
#         c=c+1
# if c:
#     o=o+ch+str(c)
# o=o.removeprefix(o[0])
# print(o)



# ns=''
# c=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c=c+1
#     else:
#         ns=ns + s[i]+str(c)
#         c=1
# ns=ns + s[len(s)-1]+str(c)
# print(ns)

# n=5
# for i in range(n):
#     print('  '*(n-i-1),end=' ')
#     for j in range((2*i) +1):
#         if i==n-1:
#             print("*",end=' ')
#         elif j%2==0:
#             print("*",end=' ')
#         else:
#             print("@",end=' ')
#     print()