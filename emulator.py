import zipfile  # Импортирует модуль zipfile для работы с ZIP-архивами
import os  # Импортирует модуль os для взаимодействия с операционной системой
import argparse  # Импортирует модуль argparse для парсинга аргументов командной строки
import csv  # Импортирует модуль csv для работы с CSV-файлами
import datetime  # Импортирует модуль datetime для работы с датами и временем
import io  # Импортирует модуль io для работы с байтовыми объектами
import tempfile  # Импортирует модуль tempfile для создания временных файлов и директорий

def load_zip_in_memory(zip_path):
    """Загружает ZIP-файл в оперативную память и возвращает объект ZipFile."""
    with open(zip_path, 'rb') as file:  # Открывает ZIP-файл в режиме чтения байтов
        zip_bytes = file.read()  # Считывает содержимое файла в память
    zip_stream = io.BytesIO(zip_bytes)  # Создает байтовой поток для работы с ZIP в памяти
    return zipfile.ZipFile(zip_stream, 'r')  # Возвращает объект ZipFile для работы с архивом

def extract_virtual(zip_file, virtual_fs):
    """Извлекает файлы ZIP-архива в оперативную память (виртуальную файловую систему)."""
    for zip_info in zip_file.infolist():  # Проходит по каждому файлу в архиве
        file_data = zip_file.read(zip_info.filename)  # Считывает содержимое файла
        virtual_fs[zip_info.filename] = file_data  # Сохраняет файл в виртуальной файловой системе

def load_config(config_path):
    """Загружает конфигурацию из CSV-файла."""
    with open(config_path, newline='') as csvfile:  # Открывает CSV-файл для чтения
        reader = csv.reader(csvfile)  # Создает объект для чтения строк из CSV
        config = {row[0]: row[1] for row in reader}  # Создает словарь с конфигурацией
    return config  # Возвращает загруженную конфигурацию

def execute_command(command, cwd, virtual_fs):
    """Выполняет команду в эмуляторе оболочки, работая с виртуальной файловой системой."""
    parts = command.split()  # Разделяет команду на части
    cmd = parts[0]  # Получает первую часть команды (имя команды)

    if cmd == 'ls':  # Если команда 'ls':
        return [f for f in virtual_fs if f.startswith(cwd)]  # Возвращает список файлов в виртуальной директории
    elif cmd == 'cd':  # Если команда 'cd':
        if len(parts) > 1:  # Проверяет, указана ли директория
            new_dir = parts[1]  # Получает имя новой директории
            new_path = os.path.join(cwd, new_dir)  # Создает путь
            if any(f.startswith(new_path) for f in virtual_fs):  # Проверяет, существует ли директория
                return new_path  # Возвращает путь к новой директории
            else:
                return f"cd: {new_dir}: No such file or directory"  # Возвращает сообщение об ошибке
        else:
            return "cd: missing argument"  # Возвращает сообщение о том, что не указан аргумент
    elif cmd == 'exit':  # Если команда 'exit'
        return "Exiting"  # Возвращает сообщение о выходе
    elif cmd == 'mkdir':  # Если команда 'mkdir'
        if len(parts) > 1:  # Проверяет, указано ли имя новой директории
            new_dir = parts[1]  # Получает имя новой директории
            virtual_fs[os.path.join(cwd, new_dir)] = None  # Создает пустую директорию в виртуальной системе
            return f"Directory {new_dir} created"  # Возвращает сообщение о создании директории
        else:
            return "mkdir: missing argument"  # Возвращает сообщение о том, что не указан аргумент
    elif cmd == 'uname':  # Если команда 'uname'
        return "Unix Emulated"  # Возвращает строку, эмулирующую Unix
    elif cmd == 'date':  # Если команда 'date'
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Возвращает текущую дату и время
    else:  # Если команда не распознана
        return f"{cmd}: command not found"  # Возвращает сообщение об ошибке

def main():
    """Основная функция для эмулятора оболочки."""
    parser = argparse.ArgumentParser(description='Shell Emulator')  # Создает парсер аргументов
    parser.add_argument('config', help='Path to the configuration CSV file')  # Добавляет аргумент для пути к конфигурационному файлу
    args = parser.parse_args()  # Парсит аргументы командной строки

    config = load_config(args.config)  # Загружает конфигурацию из указанного CSV-файла

    user = config.get('username', 'user')  # Получает имя пользователя из конфигурации, по умолчанию 'user'
    zip_path = config.get('vfs', 'vfs.zip')  # Получает путь к ZIP-файлу виртуальной файловой системы
    start_script = config.get('startscript', 'start.sh')  # Получает имя стартового скрипта

    # Загрузка виртуальной файловой системы в память
    zip_file = load_zip_in_memory(zip_path)  # Загружает ZIP-файл в память
    virtual_fs = {}  # Виртуальная файловая система как словарь
    extract_virtual(zip_file, virtual_fs)  # Извлекает архив в память

    cwd = '/'  # Текущая директория в виртуальной файловой системе

    # Выполнение стартового скрипта, если он существует
    if start_script in virtual_fs:
        for line in virtual_fs[start_script].decode('utf-8').splitlines():  # Читает команды из стартового скрипта
            command = line.strip()  # Удаляет пробелы
            result = execute_command(command, cwd, virtual_fs)  # Выполняет команду
            print(result)  # Выводит результат команды
            if command.startswith('cd '):  # Если команда 'cd'
                cwd = result if any(f.startswith(result) for f in virtual_fs) else cwd  # Обновляет текущую директорию

    # Цикл интерактивной оболочки
    print(f"{user}@emulator:{cwd}$ Type 'exit' to leave the shell.")  # Подсказка для пользователя
    while True:
        try:
            command = input(f"{user}@emulator:{cwd}$ ").strip()  # Запрашивает ввод команды у пользователя
            if command == 'exit':  # Если команда 'exit'
                print("Exiting")  # Выводит сообщение о выходе
                break  # Выходит из цикла
            result = execute_command(command, cwd, virtual_fs)  # Выполняет команду
            if isinstance(result, str) and any(f.startswith(result) for f in virtual_fs):  # Если это директория
                cwd = result  # Обновляет текущую директорию
            print(result)  # Выводит результат команды
        except Exception as e:  # Обработка исключений
            print(f"Error: {e}")  # Выводит сообщение об ошибке

if __name__ == '__main__':
    main()  # Запускает основную функцию
