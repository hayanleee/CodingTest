lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

import datetime
import re

start_time = []
end_time = []

lines.sort()
for log in lines:
    et = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}", log)
    et = datetime.datetime.strptime(et[0], "%Y-%m-%d %H:%M:%S.%f")
    log_time = re.findall("([.\d]+)s", log)
    st = et - datetime.timedelta(seconds=float(log_time[0]) - 0.001)
    start_time.append(st)
    end_time.append(et)

max_count = 1
before_1sec = datetime.timedelta(seconds=0.999)     # -1 + 0.001
all = len(start_time)
for i in range(all):
    cur_count = 0
    for k in range(all):        # 순서대로 끝점포함, 시작점포함, 전체포함
        if ((start_time[i] - before_1sec) <= end_time[k] and end_time[k] <= start_time[i]) or \
            ((start_time[i] - before_1sec) <= start_time[k] and start_time[k] <= start_time[i]) or \
            (start_time[k] <= (start_time[i] - before_1sec) and start_time[i] <= end_time[k]):
            cur_count += 1
    if max_count < cur_count:
        max_count = cur_count
print (max_count)