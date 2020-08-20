def isHoppable(arr):
    limit = len(arr)
    for i in range(len(arr)-1,-1,-1):
        if((arr[i] + i) >= limit):
            print(limit,i)
            limit = i
            if(i == 0):
                return True
			
    return False

print(isHoppable([4,2,0,0,2,0]))

print(isHoppable([3,2,0,0,2,0]))
