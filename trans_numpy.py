# import matplotlib.pyplot as plt
import numpy as np
import csv

for b in range(4):
    dataname='iqdata1_ch'+str(b+1)+'.dat'

    data = np.fromfile(dataname,dtype=np.float32) 
    data1=np.array(data)

    cnt=0
    iData=[]
    qData=[]
    for x in data1:  
        if cnt%2==0:
            iData.append(x)
        else:
            qData.append(x)
        cnt=cnt+1

    iqData=[]
    iqDataAbs=[]
    iqDataAbs_output=[]
    size=int(len(data1)/2)
    for i in range(size):
        iqData.append(complex(iData[i],qData[i]))
        iqDataAbs.append(abs(complex(iData[i],qData[i])))

    qty=120
    t=round(len(iqDataAbs)/qty,0)

    for j in range (0,len(iqDataAbs),int(t)):
        iqDataAbs_output.append(iqDataAbs[j])

    savedataname='test'+str(b+1)+'.csv'
    with open(savedataname, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(iqDataAbs_output)

    # plt.plot(iqDataAbs_output) 
    # plt.show()