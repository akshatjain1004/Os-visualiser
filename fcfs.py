

import numpy as np




print ("Enter All value with space")
inputs = np.array([int(x) for x in input().split(',')])




if len(inputs)%2 == 1:
    print ("Please input correct value, May be you missed something (You need to input even number of values, two for each process)")
else:
    print("Successfully inserted all values")
inputs




process = inputs.reshape((int(len(inputs)/2), 2)).tolist()

for p in range(len(process)):
    process[p].insert(0, p+1)

process



fcfs = sorted(process,key=lambda x: (x[1],x[2],x[0]))
fcfs




ct = []
for i in range(int(len(fcfs))):
    if i == 0:
        ct.append(fcfs[i][1] + fcfs[i][2])
    else:
        ct.append(fcfs[i][2] + ct[i-1])


for i in range(len(ct)):
    print ("Compltion time for P{} is: {}".format(fcfs[i][0],ct[i]))




tat = []
for i in range(int(len(fcfs))):
    tat.append(ct[i] - fcfs[i][1])
    
# printing Turn Around Time
for i in range(len(tat)):
    print ("Turn Around Time for P{} is: {}".format(fcfs[i][0],tat[i]))




avarage_TAT = round(np.mean(tat),2)
print ("Average Turn Around Time for all process is: ",avarage_TAT)




wt = []
for i in range(int(len(fcfs))):
    wt.append(tat[i] - fcfs[i][2])
    
# printing Waiting time
for i in range(len(wt)):
    print ("Waiting time for P{} is: {}".format(fcfs[i][0],wt[i]))





avarage_WT = round(np.mean(wt),2)
print ("Average Waiting Time for all process is:",avarage_WT)





print ("Average Waiting Time for all process is: ",avarage_WT,"sec.")
print ("Average Turn Around Time for all process is: ",avarage_TAT,"sec.")