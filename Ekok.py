def ekok(a,b):
    if a>b:
        büyük=a
    else:
        büyük=b

    while True:
        if büyük % a == 0 and büyük % b == 0:
            ekok = büyük
            break
        büyük += 1
    return ekok

print(ekok(18,30))
