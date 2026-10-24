import os
import platform
import sys
from datetime import datetime

directoria = os.getcwd()
user_ima = os.getlogin()

dla_python = sys.version

os_ima = platform.system()
os_release = platform.release()

vrema = datetime.now()
print("=== Диагностика системы ===")
print(f"Пользователь: {user_ima}")
print(f"Текущая директория: {directoria}")
print(f"Версия Python: {dla_python}")
print(f"Операционная система: {os_ima} {os_release}")
print(f"Дата и время запуска: {vrema.strftime('%Y-%m-%d %H:%M:%S')}")



C:\Users\PC\PycharmProjects\WelcomeScreen\.venv\Scripts\python.exe C:\Users\PC\PycharmProjects\WelcomeScreen\script.py 
=== Диагностика системы ===
Пользователь: PC
Текущая директория: C:\Users\PC\PycharmProjects\WelcomeScreen
Версия Python: 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)]
Операционная система: Windows 11
Дата и время запуска: 2026-09-16 22:17:48

Процесс завершен с кодом выхода 0
