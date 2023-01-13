from datetime import datetime

# start time
start_time = "00:00:00"
end_time = "01:00:00"

# convert time string to datetime
t1 = datetime.strptime(start_time, "%H:%M:%S")
print('Start time:', t1.time())

t2 = datetime.strptime(end_time, "%H:%M:%S")
print('End time:', t2.time())

# get difference
delta = t2 - t1

# time difference in seconds
print(f"Time difference is {delta.total_seconds()} detik")

ms = delta.total_seconds() / 60
print(f"Time difference is {ms} menit")

ms = delta.total_seconds() / 3600
print(f"Time difference is {ms} jam")
