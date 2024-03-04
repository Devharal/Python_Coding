import pandas as pd
import numpy as np

#1 common letters between two strings

def common_letters():
    str1=input("str1: ")
    str2=input("str2: ")
    s1=set(str1)
    s2=set(str2)
    lst=s1 & s2
    print(lst)
#common_letters()

#2 Count frequency of word in string
def freq_c():
    str1=input("str1: ")
    lst=str1.split()
    dic={}
    for i in lst:
        if i not in dic.keys():
            dic[i]=0
        dic[i]=dic[i]+1
    print(dic)
# freq_c()
    
#3 Convert list to dictionary
lst1 = ["dev", "haral", "haa"]
lst2 = [1, 2, 3]

def convert():
    dct = {}
    for i in range(len(lst1)):
        dct[lst1[i]] = lst2[i]
    print(dct)

# convert()
# using zip function
def usezep():
    result=dict(zip(lst1,lst2))
    print(result)
# usezep()

#4 find missing number in array
def get_missing_number(a):
    n=a[-1]
    total=n*(n+1)//2
    sum1=sum(a)
    print(total-sum1)
a=[1,2,4,5,6]
# get_missing_number(a)

#5 find pairs with given sum value of array

def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>sum):
            right=right+1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        elif(arr[left]+arr[right]==sum):
            print(arr[left],arr[right])
            right=right-1
            left=left+1
arr=[2,4,14,13,2,4]
sum=27
# twosum(arr,sum) Nlog(N)

# max depth of binary tree
class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

def height_tree(A):
    if(A==None):
        return 0
    else:
        ldepth=height_tree(A.left)
        rdepth=height_tree(A.right)

        if(ldepth>rdepth):
            return (1+ldepth)
        else:
            return (1+rdepth)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(7)
root.right.right=Node(6)
# print(height_tree(root))

#min difference between two element in array
def min_dif(arr):
    arr=sorted(arr)
    size=len(arr)
    min_dif=999*999

    for i in range(size-1):
        if(arr[i+1]-arr[i]<min_dif):
            min_dif=arr[i+1]-arr[i]
    return min_dif

#max difference between arrays

def max_dif(arr):
    arr=sorted(arr)
    size=len(arr)
    max_diff=-999*999

    for i in range(size-1):
        if(arr[i+1]-arr[i]>max_diff):
            max_diff=arr[i+1]-arr[i]
    return max_diff

# Rain water trap
A=[1,0,2,0,1,0,3,1,0,2]

def rain_trap(arr):
    size=len(arr)
    left=size*[0]
    rigth=size*[0]

    left[0]=arr[0]
    max_so_far_left=arr[0]
    for index in range(0,size):
        if(max_so_far_left<arr[index]):
            max_so_far_left=arr[index]
            left[index]=max_so_far_left
        else:
            left[index]=max_so_far_left
    max_so_far_right=arr[-1]
    for index in range(size-1,-1,-1):
        if(max_so_far_right<arr[index]):
            max_so_far_right=arr[index]
            rigth[index]=max_so_far_right
        else:
            rigth[index]=max_so_far_right
    
    for index in range(0,size):
        water=water+min(left[index],rigth[index]-arr[index])
    return water
# rain_trap(A)

# Hotel Booking
arr=[1,3,5]
depart=[2,6,8]
def hotel_booking(arrival,departure,k):
    event=[]
    for i in range(0,len(arrival)):
        t_arr=()
        t_arr=t_arr+(arrival[i],"RED")
        event.append(t_arr)
    for i in range(0,len(departure)):
        t_depart=()
        t_depart=t_depart+(departure[i],"BLUE")
        event.append(t_depart)
    event=sorted(event)
    guest=0

# Remove duplicate from sorted array
def remove_dup(arr):
    n=len(arr)
    if(n==0 or n==1):
        return arr
    temp=[0]*n

    pivot=0
    for last_o in range(0,n-1):
        if(arr[last_o]!=arr[last_o+1]):
            arr[pivot]=arr[last_o]
            pivot=pivot+1
    arr[pivot]=arr[n-1]
    return arr[0:pivot]


# OOPS
# Polymorphism
import pandas as pd


