# HH:MM:SS 형식
current_time = input()
lecture_start_time = input()

current = list(map(int, current_time.split(":")))
start = list(map(int, lecture_start_time.split(":")))

num = input()
t, k = map(int, num.split())

c = current[2] + current[1]*60 + current[0]*60*60
s = start[2] + start[1]*60 + start[0]*60*60

time = s - c
result = time - (t * ((100-k)/100))

if ((time < 0) or (result > 0)) :
    print(0)
else :
    print(1)