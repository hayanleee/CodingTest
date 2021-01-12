n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]

first_bus = 540
final_bus = 540 + (n-1) * t
con_time = 0
crew = []

timetable.sort()
for i in range(len(timetable)):
    crew.append(int(timetable[i][:2]) * 60 + int(timetable[i][3:]))

for times in range(n):
    if times == (n-1):      # 막차
        if m <= len(crew):
            if final_bus < crew[0]:
                con_time = final_bus
            else:
                con_time = crew[m-1] - 1
                if con_time > final_bus:
                    con_time = final_bus
        else:
            con_time = final_bus
            break
        break
    else:
        if m <= len(crew):
            for k in range(m):
                if crew[k] <= first_bus:
                    crew.pop(k)
                else:
                    break
        else:
            con_time = final_bus
            break
    con_time = first_bus
    first_bus += t
print (str(con_time // 60).zfill(2) + ":" + str(con_time % 60).zfill(2))