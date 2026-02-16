import sys
input = sys.stdin.read
data = input().split()

n, q = int(data[0]), int(data[1])

arr = list(map(int, data[2:2+n]))

prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

idx = 2 + n
res = []

for _ in range(q):
    a = int(data[idx])
    b = int(data[idx + 1])
    idx += 2

    res.append(str(prefix[b] - prefix[a - 1]))

print("\n".join(res))
