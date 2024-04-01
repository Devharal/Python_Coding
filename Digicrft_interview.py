
def gen_list(lst,n):
    for i in range(0,len(lst),n):
        print(lst[i:i+n])


l =[1,2,3,4,5,6,7,8,9]
n=4
# print(gen_list(l,n))

# Take 3*3 matrix transpose it
def tranpose_mat(mat):
    trans_mat=[[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            trans_mat[j][i]=mat[i][j]
    return trans_mat
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(tranpose_mat(mat))
