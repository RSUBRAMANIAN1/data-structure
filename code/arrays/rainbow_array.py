
arr =list(map(int,input().split()))
rainbow=[1,2,3,4,5,6,7]

k=l=len(arr)
flag=True

if(all(item in arr for item in rainbow)):
    for i in range(l):
        if(arr[i]==arr[k-1]):
           k-=1
           continue
        else:
            flag=False
else:
    flag=False
if(flag):
    print('Yes')
else:
    print('No')