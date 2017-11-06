filetext= input("enter text file name:")
handle = filetext.open()
names=[]
mydic={}
for line in handle:
    if line.startswith('From '):
        mylist= line.split()
        names.append(mylist[1])
for i in names:
    mydic[i]= mydic.get(i,0)+1
maks=max(mydic.values())
#make a list of touple to douple loop
t=mydic.items()
for a,b in t:
    if b==maks:
        print a , b 
