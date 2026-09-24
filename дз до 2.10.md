import json
import os
import platform
import psutil

def search_data():
    comp_name = platform.node() + "_"
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    free_memory = round(psutil.virtual_memory().available / (1024 ** 3), 2)
    process_count = len(psutil.pids())
    thread_count = sum(p.num_threads() for p in psutil.process_iter(['num_threads']) if p.info['num_threads'])
    
    disk_used = round(psutil.disk_usage('/').used / (1024 ** 3), 2)
   
    data = {
        "Имя компьютера": comp_name,
        "Общая память": total_memory,
        "Свободная память": free_memory,
        "Количество процессов": process_count,
        "Количество потоков": thread_count,
        "Занятая память жесткого диска": disk_used
    }
    return data

def save_data(data: dict):
    name = "data.json"
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    data = search_data()
    save_data(data)

if __name__ == "__main__":
    main()
