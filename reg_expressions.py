import re
mydata=input("Enter text file name:")
#hand=open("C:\Users\Elham\Desktop\Coursera Summer\sample.data.docx")
hand= open(mydata)
total= 0.0
count= 0
for line in hand:
    line= line.rstrip()
    nums= re.findall('[0-9]+',line)
    if len(nums)>0:
        print (nums)
        for i in range(0,len(nums)):
            int_res=int(nums[i])
            total= total+float(int_res)
            count= count+1

print("Total is:", total)
print("The number is:", count)
print("average is ", total/count)



x="From: x keshavarzi.p@gmail.com I have 2 sisters one 19 and one 42 years old"
y=re.findall('[0-9]+',x)
print(y)
z= re.search('^F.*', x)
print (z)
p= re.findall('\S+@\S+', x)
print("p is",p)
