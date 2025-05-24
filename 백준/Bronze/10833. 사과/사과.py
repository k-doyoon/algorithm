N = int(input())
ans = 0
for i in range(N):
    S,A = map(int,input().split())
    ans += A % S

print(ans)
