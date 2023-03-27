import sys
f = sys.stdin.readline

n = int(f())
nlist = list(map(int, f().split()))
m = int(f())
mlist = list(map(int, f().split()))
cnt = [0]*m

nlist.sort()

for i in range(m):
    f, b = 0, n-1

    while f<=b:
        mid = (f+b)//2
        if mlist[i] == nlist[mid]:
            cnt[i] += 1
            break
        elif mlist[i] > nlist[mid]:
            f = mid+1
        else:
            b = mid-1

for i in cnt:
    print(f"idx= {i} ")