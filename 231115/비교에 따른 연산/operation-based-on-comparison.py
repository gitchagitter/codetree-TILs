a=input()
aa=a.split()
q=int(aa[0])
w=int(aa[1])
if q>w:
    q=(q*w)
    print(q)
else:
    w=(w/q)
    print(w)