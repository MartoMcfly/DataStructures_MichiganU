fname = input("Enter file name: ")
fh = open(fname)
c = 0
lst = list()
for line in fh:
    for i in line.rstrip().split():
        if i not in lst:
            lst.append(i)
            
        c = c + 1
lst.sort()
print(lst)
