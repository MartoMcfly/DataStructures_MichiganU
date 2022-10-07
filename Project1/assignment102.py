x , y = 3, 4
print(type(x))

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print( y)

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
c = 0
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        c = c + 1
        print(str(line[-2]))
        count[str(line[-2])] = count.get(str(line[-2]),0) + 1
        
print(count)
