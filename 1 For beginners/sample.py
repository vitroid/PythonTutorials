file = open("sample1.txt")
sum0 = 0
sum1 = 0
sum2 = 0
for line in file:
    columns = line.split()
    col0 = float(columns[0])
    col1 = float(columns[1])
    col2 = float(columns[2])
    sum0 += col0        
    sum1 += col1
    sum2 += col2
    print col0+col1+col2
    print sum0,sum1,sum2
