play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

import re

stack = [0] * len(logs)
start_time = []
end_time = []
logs.sort()
for log in logs:
    se = re.findall(r"\d{2}:\d{2}:\d{2}", log)
    start_time.append(int(se[0].replace(":","")))
    end_time.append(int(se[1].replace(":","")))

adv = int(adv_time.replace(":",""))

if end_time[-1] - start_time[0] <= adv:
    print("00:00:00")
    # return "00:00:00"

for i in range(len(start_time)):
    adv_s = start_time[i]
    adv_e = start_time[i] + adv
    tt = 0
    for k in range(len(start_time)):
        if k < i:
            for idx in range(i-1):
                if end_time[idx] >= adv_s:
                    tt += adv_s - end_time[idx]
        else:
            if end_time[k] < adv_e:
                if start_time[k] > adv_s:
                    tt += end_time[k] - start_time[k]
                else:
                    tt += end_time[k] - adv_s
            else:
                if start_time[k] < adv_e:
                    tt += adv_e - start_time[k]
    stack[i] = tt

ind = stack.index(max(stack))
print(logs[ind][:8])



# ---- 최대 24시간으로 봤음...

# import datetime
# import re
#
# stack = [datetime.datetime.strptime("00:00:00", "%H:%M:%S")] * len(logs)
# start_time = []
# end_time = []
# logs.sort()
# for log in logs:
#     se = re.findall(r"\d{2}:\d{2}:\d{2}", log)
#     start_time.append(datetime.datetime.strptime(se[0], "%H:%M:%S"))
#     end_time.append(datetime.datetime.strptime(se[1], "%H:%M:%S"))
#
# adv = re.findall(r"\d{2}", adv_time)
# tmpadv = datetime.timedelta(hours=int(adv[0]), minutes=int(adv[1]), seconds=int(adv[2]))
#
# if end_time[len(end_time)-1] - start_time[0] <= tmpadv:
#     print("00:00:00")
#     # return "00:00:00"
#
# for i in range(len(start_time)):
#     adv_s = start_time[i]
#     adv_e = start_time[i] + datetime.timedelta(hours=int(adv[0]), minutes=int(adv[1]), seconds=int(adv[2]))
#     for k in range(len(start_time)):
#         if k < i:
#             for idx in range(i-1):
#                 if end_time[idx] >= adv_s:
#                     stack[i] += adv_s - end_time[idx]
#         else:
#             if end_time[k] < adv_e:
#                 stack[i] += end_time[k] - start_time[k]
#             else:
#                 stack[i] += adv_e - start_time[k]
#
# result = start_time[stack.index(max(stack))].time()
#
# print(result)
# print(str(result))

