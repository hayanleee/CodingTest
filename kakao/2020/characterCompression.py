# 문자열 len 글자 단위로 자르는 방법
# list(map(''.join, zip(*[iter(s)] * i)))

s = "ababcdcdababcdcd"
if len(s) == 1:
    print(1)
    # return 1
n = len(s) // 2
answer = []
for length in range(1, n+1):
    print([s[i:i+length] for i in range(0, len(s), length)])
    stack = ''
    ssplit = [s[i:i+length] for i in range(0, len(s), length)]
    tmp = ''
    cnt = 1
    for k in range(len(ssplit)):
        if tmp == ssplit[k]:
            cnt += 1
        else:
            if cnt == 1:
                stack += tmp
            else:
                stack += str(cnt) + tmp
            tmp = ssplit[k]
            cnt = 1
    else:
        if cnt == 1:
            stack += tmp
        else:
            stack += str(cnt) + tmp
    print(stack)
    answer.append(len(stack))

print(min(answer))



