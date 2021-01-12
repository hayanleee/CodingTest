user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

# ["frodo", "fradi", "crodo", "abc123", "frodoc"]   ["fr*d*", "abc1**"]     2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3

import itertools

def matching(user, ban):
    for u, b in zip(user, ban):
        u = list(u)
        b = list(b)
        if len(u) != len(b):
            return False
        for i in range(len(u)):
            if u[i] == b[i]:
                continue
            else:
                if b[i] == '*':
                    continue
                else:
                    return False
    else:
        return True

answer = []
combi = list(itertools.permutations(user_id, len(banned_id)))
for user in combi:
    if matching(user, banned_id):
        answer.append(list(user))
else:
    print(answer)
    print(set([tuple(set(a)) for a in answer]))
    print(len(set([tuple(set(a)) for a in answer])))
