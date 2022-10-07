name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        
        count[line.split()[1]] = count.get(line.split()[1],0) + 1

bigKey = 0
bigNumber = 0
for key in count:
    if count[key] > bigNumber:
        bigNumber = count[key]
        bigKey = key
print(bigKey + ' ' + str(bigNumber))