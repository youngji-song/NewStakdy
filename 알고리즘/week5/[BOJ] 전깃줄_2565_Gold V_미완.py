# 전깃줄 (G5)
# 23:34~

n = int(input())
electric = [list(map(int, input().split())) for _ in range(n)]
electric.sort()

A = []  # i >= j
B = []  # i <= j

for ele in electric:
    if ele[0] >= ele[1]:
        A.append(ele)
    elif ele[0] <= ele[1]:
        B.append(ele)

print()
print(A)
print(B)

for idx in range(len(A)-2):
    # print(idx+1)
    if A[idx][1] > A[idx+1][1]:
        # and A[idx][0] == A[idx][1]:
        A.pop(idx)
for idx in range(len(B)-2):
    if B[idx][1] < B[idx+1][1]:
    # and B[idx][0] == B[idx][1]:
        B.pop(idx)

print()
print(A)
print(B)


print(n-max(len(A),len(B)))