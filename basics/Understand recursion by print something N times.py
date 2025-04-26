#natural nums
def natural(n):
    if n <= 0: return
    natural(n-1)
    print(n,end=" ")

natural(10)


#name n times.
def nameNtimes(n):
    if n <= 0: return
    print("mohan")
    nameNtimes(n-1)
nameNtimes(5)


#reverese natural times.
def nameNtimes(n):
    if n <= 0: return
    print(n)
    nameNtimes(n-1)
nameNtimes(5)