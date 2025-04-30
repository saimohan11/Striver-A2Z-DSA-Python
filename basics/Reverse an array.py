def rev(x,n):
    ans = [0] * n
    for i in range(n-1,-1,-1):
        ans[n-i-1] = x[i]
    print(ans)

x = [1,2,3,4,5]
n = len(x)
rev(x,n)