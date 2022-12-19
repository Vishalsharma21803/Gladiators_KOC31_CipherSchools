# list of list or 2-d array

listoflist=[[1,2,3],[4,5,6],[7,8,9],[10,11]]
sum=0
for i in listoflist:
    for j in i:
        sum+=j
    print(sum)
    print()
