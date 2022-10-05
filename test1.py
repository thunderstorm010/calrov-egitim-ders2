import threading

i = 0
lock = threading.Lock()
event = threading.Event()
event.wait()

def hello2():
    global i
    while True:
        lock.acquire()
        print(f"{i}")
        i += 1
        lock.release()

def hello():
    global i
    while True: 
        with lock:
            print(f"{i}")
            i += 1

thread = threading.Thread(target=, args=, daemon=)
thread2 = threading.Thread(target=hello)
thread.start()
thread.join()
thread2.start()
