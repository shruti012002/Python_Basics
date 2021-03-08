#patterns
"""i=1
while(i<=4):
    j=1
    while(j<=4):
        print("#",end=" ")
        j+=1
    i+=1
    print()

for i in range(0,4):  #for i in range(4): can also be used
    for j in range(0,4):   #for j in range(4): can also be used
        print("#",end=" ")
    print()

i=1
while(i<=4):
    j=1
    while(j<=i):
        print("#",end=" ")
        j+=1
    i+=1
    print()

for i in range(1,5):
    for j in range(i):
        print("#",end=" ")
    print()"""

for i in range(4,0,-1):  #for i in range(4): can also be used as it will iterate from 0 then 1,.....upto 3
    for j in range(i):   #for j in range(4-i): can also be used
        print("#",end=" ")
    print()