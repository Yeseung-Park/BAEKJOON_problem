H, M = map(int, input().split())

new_M = M-45

if new_M < 0:
    new_H = H-1
    new_M = 60+(new_M-45)

if new_H < 0:
    new_H = 24+new_H



print(new_H, new_M)