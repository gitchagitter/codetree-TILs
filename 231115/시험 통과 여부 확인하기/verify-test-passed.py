a=input()
a=int(a)
if a>=87:
    print("pass")
else:
    a-=87
    a=(a*a/2)
    print(f"{a} more score")