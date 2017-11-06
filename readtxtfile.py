fname =input("Enter the file name:")
try:
    hfile=open(fname)
except:
    print("The file you entered does not exist!")
    exit()
count =0
for line in hfile:
    count = count+1
print("There are: ", count, " lines in this file")
#read the file means copying open it is connecting
#Strip helps to remove double spacing 
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line= line.strip()
    print(line.upper())
