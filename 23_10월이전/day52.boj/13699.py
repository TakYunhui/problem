n = int(input())
t = [0] * 36
t[0] = 1
t[1] = 1
t[2] = 2
t[3] = 5
'''
t[4] = [0]*[3] + [1]*[2] + [2]*[1] + [3]*[0] = 14 
for k in range(i):
    t[i] += t[k] * t[k-1-i]
'''
if n > 1:
    for i in range(4, n+1):
        for k in range(i):
            t[i] += t[k] * t[i-1-k]

print(t[n])