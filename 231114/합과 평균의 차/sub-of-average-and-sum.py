a=input()
aa=a.split()
q=int(aa[0])
w=int(aa[1])
e=int(aa[2])

u=int(q+w+e)
i=int(u/len(aa))

print(u)
print(i)
print(f"{u-i}")