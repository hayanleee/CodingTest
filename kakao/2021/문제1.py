import re
new_id = "z-+.^."

tmp = new_id.lower()
tmp = re.sub('[^0-9a-zA-Zㄱ-힗-_.]', '', tmp)
tmp = re.sub('[.]+', '.', tmp)
if tmp.startswith('.'):
    tmp = tmp[1:]
if tmp.endswith('.'):
    tmp = tmp[:-1]
if len(tmp) == 0:
    tmp = 'a'
if len(tmp) > 15:
    tmp = tmp[:15]
    if tmp.endswith('.'):
        tmp = tmp[:-1]
if len(tmp) < 3:
    tmp = tmp + (tmp[-1] * (3 - len(tmp)))

print(tmp)