
from collections import Counter
for _ in range (int(input())):
    s = input()
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2 if(len(s)%2==0)
                else
                    (len(s)//2 +1):]
    print(Counter(s1))
    print(Counter(s2))
    