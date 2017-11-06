# This application will read the mailbox data (mbox.txt) count up the number email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#Use file text myinbox.txt which i copied from the url http://www.pythonlearn.com/code/mbox.txt

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
	DROP TABLE IF EXISTS Counts''')

cur.execute('''
	CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = raw_input('Enter file name: ')
while(len(fname) < 1):
	print 'Please enter file name again!'

fh = open(fname)

corporation = list()

for line in fh:
	if line.startswith('From: '):
		pieces = line.split()
		email = pieces[1]
		index = email.find('@')
		corporation.append(email[index+1:len(email)])
corporation = list(set(corporation))

number = dict.fromkeys(corporation, 0)
fh = open(fname)
for line in fh:
	if line.startswith('From: '):
		pieces = line.split()
		email = pieces[1]
		index = email.find('@')
		for item in number.keys():
			if email[index+1:len(email)] == item:
				number[item] = number[item] + 1


for item in number.keys():
	cur.execute('''INSERT INTO Counts(org, count) VALUES(?, ?)''', [item,number[item]])
	conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
	print str(row[0]),row[1]

cur.close()
