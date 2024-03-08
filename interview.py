# List of intergers all possible combination of sublist within that list print max possible sum 
l=[1,2,3,4,5]
# print(sum(l))
def sublist(lst):
    n=len(lst)
    sublist1=[]
    
    for i in range(n):
        for j in range(i+1,n+1):
            sublist1.append(lst[i:j])
        
    return sublist1
l1=sublist(l)
# print(len(l1))
sum1=[]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        sum1.append(sum(l1[j]))
# print(max(sum1))

# string of alphabets you have to print the frequency of each alphabet that is occuring string but the string must be passed only once

s="adasdajnfdjnf"

def count(s):
    cnt={}

    for i in s:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1
    return cnt
# print(count(s))

# 3, 2d matrix of numbers we have to print numbers in spiral manner from [0,0] element and go clockwise fashion

mat=[[1,3,3,5,6],[2,3,5,6,7],[1,3,7,5,1],[1,5,3,8,6],[2,6,8,9,0]]

def spiral(mat):
    m=len(mat)
    n=len(mat[0])

    if (len(mat)==0):
        return mat
    l=0
    r=n-1
    t=0
    b=m-1
    

    while l<=r and t<=b:
        # left to right
        for i in range(l,r+1):
            print(mat[t][i])
        t=t+1
        # traversing top to bottom
        for i in range(t,b+1):
            print(mat[i][r])
        r=r-1
        # travesring right to left
        for i in range(r,l,-1):
            print(mat[b][i])
        b=b-1
        # traversing bottom to top
        for i in range(b,t,-1):
            print(mat[i][l])
        l=l+1
            
            

print(spiral(mat))




