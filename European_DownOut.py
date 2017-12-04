import numpy as np


K = 100
T = 1
S = 100
sig = 0.2
r = .06
div = .03
H = 99
N = 10
M = 100

dt = T/N
nudt = (r - div - (0.5*(sig**2)))
sigsdt = (sig * np.sqrt(dt))

sum_CT = 0
sum_CT2 = 0

for j in range(M):
    St = S
    Barrier_Crossed = False
    for i in range(N):
        epsilon = np.random.normal()
        St = St * np.exp(nudt + sigsdt * epsilon)
        if (St <= H):
            Barrier_Crossed = True
            break
    if Barrier_Crossed:
        CT = 0
    else:
        CT = np.maximum(0, St - K)
    sum_CT = sum_CT + CT
    sum_CT2 = sum_CT2 + CT*CT

call_value = sum_CT / M * np.exp(-r * T)
SD = np.sqrt((sum_CT2 - sum_CT * sum_CT / M) * np.exp(-2 * r * T) / (M - 1))
SE = SD / np.sqrt(M)

print(call_value)
print(sum_CT)
