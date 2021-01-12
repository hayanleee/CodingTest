A = [5, -5]

left_number = 0
right_number = sum(A)
abslist = []
for i in A:
    left_number += i
    right_number -= i
    abslist.append(abs(left_number - right_number))
abslist.pop()
print(min(abslist))
# return min(abslist)
