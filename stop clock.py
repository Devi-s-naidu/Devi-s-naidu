import time
n = int(input("enter the seconds"))
for i in range(n, 0, -1):
    print(i)
    time.sleep(1)
print("time up")