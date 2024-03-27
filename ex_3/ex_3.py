# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, 
# переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, 
# INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, 
# щоб отримати всі записи цього рівня.

# Вимоги до завдання:
#   Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
#   Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. 
# Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. 
# Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
#   Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування 
# (INFO, ERROR, DEBUG, WARNING).
#   Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
#   Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
#   Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
#   Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
#   Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. 
# Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. 
# Вона приймає результати виконання функції count_logs_by_level.


from pathlib import Path
from collections import Counter
import sys

def load_logs(file_path: str) -> list:                                          #define function for load logs from file
    path = Path(file_path)                                                      #get Path string
    path = path.absolute()                                                      #recive absolut file Path
    try:                                                                        #try work with file
        with open(path,"r",encoding="utf-8") as log_file:                       #open file
            logs = [parse_log_line(line.replace("\n","")) for line in log_file]                 #load records to list and remove "new line" sign. 
    except FileNotFoundError:                                                   #catch exeption
        print("File not found")                                                 #mesage to user
    return logs                                                                 #return list records

def parse_log_line(line: str) -> dict:                                          #define parser function
    try:                                                                        #try split, create dictionary and return
        list = line.split(" ",3)                                                #normal record splited on 4 pieces
        return {"date":list[0] + " " + list[1], "level":list[2], "msg":list[3]} #1,2 - date and time, 3 - level, 4 - message
    except Exception:                                                           #catch exeption
        print("Can't split log record")                                         #mesage to user

def filter_logs_by_level(logs: list, level: str) -> list:                       #define function for filtering log records
    return filter(lambda x:x.get("level")==level,logs)                          #return list of filtered logs

def count_logs_by_level(logs: list) -> dict:                                    #define function for statistic
    levels = [el.get("level") for el in logs]                                   #generate list of level records
    return Counter(levels)                                                      #return dictionary with statistic

def print_statistic(statistics:dict):                                           #define function for print statistic
    print(f"Рівень логування | Кількість записів")                              #print header
    print(f"{"-"*17}|{"-"*18}")                                                 
    for key, val in statistics.items():                                         #print each record from statistic with formating
        print(f"{key:<17}| {val:<17}")

def print_records(records:list):                                                #define function for print records from list
    for el in records:                                                          #print each record
        print(f'{el["date"]} {el["level"]} {el["msg"]}')

def main():                                                                     #define main logic
    if len(sys.argv)>=2:                                                        #if script run with 1 additional parameter
        path = sys.argv[1]                                                      #get path to file
        logs = load_logs(path)                                                  #load logs from file
        level = None                                                            #set default level
        if len(sys.argv)>=3:                                                    #if have 2 additional parameters
            level = sys.argv[2].upper()                                         #get level
        print_statistic(count_logs_by_level(logs))                              #print statistic 
        if level is None:                                                       #if level not select
            print(f"\nДеталі логів:")                                             
            print_records(logs)                                                 #print all record from file
        else:
            print(f"\nДеталі логів для рівня {level}:")
            print_records(filter_logs_by_level(logs, level))                    #print filtered records for selected level

main()                                                                          #run code