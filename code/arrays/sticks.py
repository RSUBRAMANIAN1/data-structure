###
# codechef is need to maximize the given sticks and build and a rectangle usiing it.
# greedy algorithm to be used.



l = int(input())
arr = list(map(int, input().split()))
area = 1
freq = [0]*1001
flag = False
isDone =False
count = 0
le=1000
for i in arr:
    freq[i] += 1
    # while(le>=0):
    #     le=le-1
    #     if(not flag):
    #         if(freq[le]>=2):
    #             area*=le
    #             flag=True
    #             freq[le]-=2
    #     if(flag):
    #         if(freq[le]>=2):
    #             area*=le
    #             isDone=True
    #             break
    # if(isDone):
    #     print(area)
    # else:
    #     print(-1)

    # method 1:
le=len(freq)-1
while( le>=0 and flag == False):
    if(freq[le] >= 4 and count == 0):
        area *= le**2
        flag = True
        break
    if(freq[le]>= 2):
        area *= le
        freq[le] -= 2
        count+=1
        if(count == 2):
            flag = True
        
    le=le-1
    
if(flag):
    print(area)
else:
    print(-1)



