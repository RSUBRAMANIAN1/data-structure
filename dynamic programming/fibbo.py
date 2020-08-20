# def fibbo(n):
#     m=[0]*(n+1)
#     m[0]=1                        #Bottom-up method
#     m[1]=1
#     for j in range(2,n+1):
# 	    m[j]=m[j-1]+m[j-2]
    
#     return m[n-1]

# print(fibbo(35))

def fibbo(n,m):
    if(m[n]!=None):
        return m[n]
    if(n==1 or n==2):
        return 1
    else:
        result=fibbo(n-1,m)+fibbo(n-2,m)
        m[n]=result
    return result


n=1000
m=[None]*(n+1)
print(fibbo(n,m))

