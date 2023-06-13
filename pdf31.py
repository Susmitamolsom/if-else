# num=int(input("enter no"))
# if num%5==0:
#     print("hello")
# else:
#     print("bye")


# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print("",end=" ")
#         j=j-1
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k=k+1
#     print()
#     i=i-1
for i in range(5):
    for j in range(i):
        print("",end=" ")
    for k in range((5-i)-1):
        print("*",end=" ")
    print( )
#     n=int(input("enter rows"))
# for i in range(n):
#     for b in range(i):
#         print(" ",end=" ")
#     for j in range(2*(n-i)-1):
#         print("*",end=" ")
#     print()        