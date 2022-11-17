import time


def time_convert(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("time lapsed={0}:{1}:{2}".format(int(hours), int(minutes), seconds))


input("press enter to start")
start_time = time.time()
input("press enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
