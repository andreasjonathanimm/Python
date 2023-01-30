import math
prime=[]
number=int(input("Prime numbers limit: "))
for num in range(3,number,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        prime.append(num)
for p in prime:
    print(p,end=" ")