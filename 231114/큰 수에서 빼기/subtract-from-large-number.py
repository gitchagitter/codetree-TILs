a=input().split()
q=int(a[0])
w=int(a[1])
if q>w:
    qq=(q-w)
    print(qq)
if q<w:
    ww=(w-q)
    print(ww)
if q==w:
    print(0)