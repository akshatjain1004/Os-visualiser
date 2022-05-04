s= list(map(str, input().split(',')))
status=[]
frames= int(input())

Frame=[]
for i in range(frames):
    Frame.append(" ")
count=0
for i in s:
    temp= True
    for j in Frame:
        if(j==i):
            status.append('hit')
            temp= False
    if(temp):
        status.append('fault')
        Frame[count]=i
        count= (count+1)%frames
    print(Frame)
print(status)