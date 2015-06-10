def transpose(matrix, default=None):
    #列数の最大値を調べる。
    maxc = 0
    for row in matrix:
        if maxc < len(row):
            maxc = len(row)
    #コラムの数は列数の最大値
    columns = [[] for i in range(maxc)]
    for row in matrix:
        for i in range(maxc):
            if i < len(row):
                columns[i].append(row[i])
            else:
                #データが足りない部分はdefault値を入れる
                columns[i].append(default)
    return columns

