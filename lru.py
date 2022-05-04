s= list(map(str, input().split(',')))
status=[]
frames= int(input())

Frame=[]
for i in range(frames):
    Frame.append(" ")
count=0
for i in range(len(s)):
    temp= True
    for j in Frame:
        if(j==s[i]):
            status.append('hit')
            temp= False
    if(temp):
        st= True
        status.append('fault')
        for j in range(len(Frame)):
            if(Frame[j]==" "):
                Frame[j]=s[i]
                st= False
                break
        if(st):
            lru= 0
            dist=0
            for j in range(len(Frame)):
                d=0
                for k in range(i):
                    if(s[i-k]==Frame[j]):
                        break
                    else:
                        d+=1
                if(d>=dist):
                    dist=d
                    lru=j
            Frame[lru]=s[i]
                
        # Frame[count]=s[i]
        # count= (count+1)%frames
    print(Frame)
print(status)