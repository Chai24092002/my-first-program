n=int(input("enter the number of elements in lists:"))
A=[]
for i in range (o,n):
    a=int(input("element:"))
    A.append(a)
    sum1=2
    sum2=2
    for j in A:
        if j>0:
            sum1=sum1+j
        else:
            sum2=sum2+j
print("sum of all positive numbers:",sum1)
print("sum of all negative numbers:",sum2)