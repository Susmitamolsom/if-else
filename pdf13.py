amt=int(input("enter"))
if amt>0:
    a=amt//2000
    b=amt%2000
    c=b//500
    d=b%500
    e=c//200
    f=c%200
    g=e//100
    h=e%100
    i=g//50
    j=g%50
    k=i//20
    l=i%20
    m=k//10
    n=k%10
    o=m//5
    p=m%5
    print("notes of 2000",b,"notes of 500",d,"notes of 200",f,"notes of 100",h,"notes of 50",j,"notes of 20",l,"notes of 10",n,"notes of 5",p)
