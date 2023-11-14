a=input().split()
q=int(a[0])
w=int(a[1])
if q>=w:
    q=(q-w)
    print(q)
if q<w:
    w=(w-q)
    print(w)