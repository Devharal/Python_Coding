# Amstrong Number
# 153=(1**3)+(5**3)+(3**3)

# user=int(input("Enter your Number:"))
# n=user
# a=n%10  #Reminder dete
# n=n//10  #Quotient dete
# b=n%10
# c=n//10

# if (a**3)+(b**3)+(c**3)==user:
#     # print("Agya")

#  Narcissictic number
# 100-1000 Amstrong number
# for num in range(100,1000):
#     i=num
#     a=num%10
#     num=num//10
#     b=num%10
#     c=num//10
#     if (a**3)+(b**3)+(c**3)==i:
#         print(i)

# Popolation
# flag=0
# a=10000
# print(a)
# while True:
#     b=(a)-((10*a)/100)
#     a=b
#     print(int(b))
#     flag=flag+1

#     if flag==100:
#         break

d={'a':100,'b':200,'c':300}

max_v=max(d.values())
min_v=min(d.values())

for i in d:
    if d[i]==max_v:
        print((d[i]))
        break

for j in d:
    