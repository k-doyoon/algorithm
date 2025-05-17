n = int(input())
ans = 0 
a ,b ,c= map(int,input().split())

if a<n:
    ans += a
else :
    ans += n


if b<n:
    ans += b
else :
    ans += n


if c<n:
    ans += c
else :
    ans += n


print(ans)
