n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# secret_map = []
# for i in range(n):
#     temp = format(arr1[i] | arr2[i], 'b').replace("0", " ").replace("1", "#")
#     secret_map.append(temp.rjust(n))
# print(secret_map)

secret_map = [format(arr1[i] | arr2[i], 'b').replace("0", " ").replace("1", "#").rjust(n) for i in range(n)]
print(secret_map)