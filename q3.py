def fn(lst) : 
    res = [] 
    seen = set() 
    for it in lst :
        if it not in seen :
            seen.add(it) 
            res.append(it)
    return res

ln = [2,3,56,1,4,2,56,98,2,1]
print(fn(ln))