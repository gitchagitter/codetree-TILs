d=input().split()
m=int(d[0])  #178
g=int(d[1]) 
 #88
mm=(m*0.01)
tt=(mm**2)
u=int(g/tt)


print(u)
if u>25:
    print("Obesity")