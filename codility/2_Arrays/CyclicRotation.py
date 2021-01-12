A = [9,7,6,3,8,5,5]
K = 4

if len(A) == 0:
    # return []
    print([])
remainder = K % len(A)
if remainder == 0:
    # return A
    print(A)
rotate = A[-remainder:] + A[:-remainder]
# return rotate
print(rotate)