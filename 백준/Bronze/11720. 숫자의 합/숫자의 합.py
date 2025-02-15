d = int(input())
k = int(input())
s = 0
while k > 0 :
    a = k % 10
    s += a
    k = k // 10
print(s)
