def mysplit(strng):
    i = 0
    lst = []
    while i != -1:
        x = strng.find(" ", i)        
        if x != -1:
            st = strng[i:x]
            i = x+1
            if st == '':
                continue
            else:
                lst.append((st))
        else:
            st = strng[i:]
            i = x
            if st == '':
                continue
            else:
                lst.append((st))
    
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
