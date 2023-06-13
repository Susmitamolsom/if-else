# a=int(input("enter 1st no"))
# b=int(input("enter 2nd no"))
# if a>b and b<a:
#     print(a)
# else:
#     print("none")
# i=1
# a=1
# c=0
# sum=0
# l=4000000
# while i<l:  
#     if i%2==0:
#         sum=sum+i
#     c=i+a
#     i=a
#     a=c
# # print(sum)
# i=2
# n=600851475143
# while i<n:
#     if n%i==0:
#         n=n//i
#     i=i+1
# # print(n)
# i=1
# a=0
# sum=0
# c=1
# while i<=1000:
#     a=c+a
#     i=i+1
#     c=i**i
# print(a)
i=100
p=1
sum=0
while i>=1:
    p=p*i
    i=i-1   
print(p)
a=str(p)
b=0
while b<len(a):
    c=a[b]
    sum=sum+int(c)
    b=b+1
print(sum)