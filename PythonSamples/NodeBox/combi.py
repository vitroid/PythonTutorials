def combinations(elems, n):
    result = []
    if n == 1:
        for i in elems:
            result.append([i])
    else:
        tmp = list(elems)
        while len(tmp) > 0:
            head = tmp.pop(0)
            print head,tmp
            sub = combinations(tmp,n-1)
            print "sub", sub
            for i in sub:
                result.append(i+[head])
    print elems, n, "=>", result
    return result


combinations([1,2,3,4,5,6],3)
