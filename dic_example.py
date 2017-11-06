name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mylist=[]
for line in handle:
    if line.startswith('From '):
        linelist = line.split()
        mylist.append(linelist[1])
mydic= {}
for i in mylist:
    mydic[i]= mydic.get(i, 0)+1
bb= max(mydic.values())
#make touple, search through i,j
lastlist = mydic.items()
for i,j in lastlist:
    if j==bb:
        print i, j
