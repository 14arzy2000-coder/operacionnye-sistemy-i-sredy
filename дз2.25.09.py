import multiprocessing as mp
import os
import time
def welcome():
    print(f"Старт welcome, PID: {os.getpid()}, PPID: {os.getppid()}")
    time.sleep(2)

def work():
    print(f"Старт work, PID: {os.getpid()}, PPID: {os.getppid()}")
    time.sleep(2)

def finish():
    print(f"Старт finish, PID: {os.getpid()}, PPID: {os.getppid()}")
    time.sleep(2)

def main():
    print(f"Главный процесс PID: {os.getpid()}")
    p1 = mp.Process(target=welcome)
    p2 = mp.Process(target=work)
    p3 = mp.Process(target=finish)

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()

if __name__ == "__main__":
    main()
