str1 = "handshake"
str2 = "shake hands"

import re
arr1 = []
arr2 = []
for i in range(len(str1) - 1):
    arr1.extend(re.findall("[a-z]{2}", str1[i:i+2].lower()))
for i in range(len(str2) - 1):
    arr2.extend(re.findall("[a-z]{2}", str2[i:i+2].lower()))

total = len(arr1) + len(arr2)
intersec = 0
for element in arr1:
    for i in range(len(arr2)):
        if arr2[i] == element:
            intersec += 1
            arr2.pop(i)
            break
union = total - intersec    # 합집합개수 = 원소총개수 - 교집합개수
if not union:
    print (65536)
Jaccard = (float(intersec) / union) * 65536
print (int(Jaccard))