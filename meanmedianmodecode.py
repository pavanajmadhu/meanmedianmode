import csv

#calculating mean

with open("data.csv",newline="") as i:
    reader=csv.reader(i)
    file_data=list(reader)

file_data.pop(0)

newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

totalnoofvalues=len(newdata)
total=0
for i in newdata:
    total+=i

mean=total/totalnoofvalues
print("mean is : ",mean)



#calculating median

with open("data.csv",newline="") as a:
    reader=csv.reader(a)
    file_data=list(reader)

file_data.pop(0)

newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

n=len(newdata)
newdata.sort()

if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2

else:
    median=newdata[n//2]

print("median is ", median)

#calculating mode



from collections import Counter


with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

#print(file_data)
newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))

data=Counter(newdata)
modedataforrange={
    "65-75":0,
    "75-85":0,
    "85-95":0
}
for height,occurence in data.items():
    if 65<float(height)<75:
        modedataforrange["65-75"]+=occurence
    
    elif 75<float(height)<85:
        modedataforrange["75-85"]+=occurence    

    elif 85<float(height)<95:
        modedataforrange["85-95"]+=occurence    

moderange,modeoccurence=0,0

for range,occurence in modedataforrange.items():
    if occurence>modeoccurence :
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((moderange[0]+moderange[1])/2)
print("mode is : " , mode)
