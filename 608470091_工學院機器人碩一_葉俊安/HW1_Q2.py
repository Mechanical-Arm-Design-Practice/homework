Tom_list = [80,100,90,95]

John_list = [100,93,75,80]

d1 = {"Tom":Tom_list,"John":John_list}

for i in d1:
    print(i+"\nValue: ")
    sum = 0
    for j in d1[i]:
        print(str(j))
        sum+=j
    print("AVG: "+str(sum/len(d1[i])))    

#print ("Tom value : ",d1["Tom"],"Tom AVG : ",Tom_AVG)
#print ("John value : ",d1["John"],"John AVG : ",John_AVG)