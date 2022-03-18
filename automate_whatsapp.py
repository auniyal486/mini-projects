test_cases=int(input())
arr1=[0]*test_cases
arr4=[0]*test_cases
for i in range(test_cases):
    arr1[i]=int(input())
    best=float("inf")
    poistion=-1
    arr2=[(0,0)]*arr1[i]
    arr3=[(0,0)]*arr1[i]
    for j in range(arr1[i]):
        arr2[j][0]=int(input())
    for j in range(arr1[i]):
        arr2[j][1]=int(input())
        arr3[j]=(0,round(arr2[j][1]/arr2[j][0],2))
        if arr3[j][1]<best:
            best=arr3[j][1]
            poistion=j
    arr3=sorted(arr3,key=lambda x:x[1])
    cost=0
    total_covered=0
    for j in range(arr1[i]):
        distance=arr2[(j+poistion)%arr1[i]][0]
        cost+=distance*arr2[(j+poistion)%arr1[i]][0]
        
