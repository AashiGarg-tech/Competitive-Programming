import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

log = [0] * (n + 1)
for i in range(2, n + 1):
    log[i] = log[i // 2] + 1

K = log[n] + 1
st = [[0] * K for _ in range(n)]

for i in range(n):
    st[i][0] = arr[i]

j = 1
while (1 << j) <= n:
    i = 0
    while i + (1 << j) <= n:
        st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        i += 1
    j += 1

answers = []

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    length = r - l + 1
    k = log[length]

    ans = min(st[l][k], st[r - (1 << k) + 1][k])
    answers.append(str(ans))

print("\n".join(answers))
