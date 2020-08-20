if __name__=='__main__':

    #array=list(map(int,input().split()))
    s=input()

    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
            #array1.remove('[')