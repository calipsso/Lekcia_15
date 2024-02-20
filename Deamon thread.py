import threading
import time

def backGroundTask():
    while True:
        print("Daemon is running")
        time.sleep(2)

deamon_thread = threading.Thread(target=backGroundTask, args=(), daemon= True)
deamon_thread.start()

print("Zacni program")
time.sleep(11)
print("Ukonci program")