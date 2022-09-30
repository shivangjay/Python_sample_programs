from itertools import combinations

s = "232387421"
n = 9
m = 2
k = 3

s = list(s)
for i in range(len(s)):
    s[i] = int(s[i])
i = 0
li = []
while i < n:
    if s[i] % 2 == 0:
        for j in range(i + (m - 1), n):
            if s[j] % 2 != 0:
                li.append(s[i:j + 1])
                i = j
                break
        i = i + 1
    else:
        i = i + 1
print(li)
if len(li) == k:
    print(k)
elif len(li) > k:
    temp = len(li) - k
    lit = []
    for i in range(k):
        lit.append(i+1)
    comb = combinations(lit, temp)
    print(len(list(comb)))
