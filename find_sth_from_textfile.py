# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count+1
        pos=line.find("0.")
        n= line[pos:pos+6]
        fn=float(n)
        total=total+fn
ave= total/count
print"Average spam confidence:", ave
