a=input().split()
z=int(a[0])  # a.split()로 리스트 구분하면 훨씬 편함
x=int(a[1])
l=len(a)
v=int(z+x)
n=float(v/l)  #f로 {}내에서 계산 가능함 단 꼭{} 여기서만 해야함



print(v,n)