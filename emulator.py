import zipfile  # Импортирует модуль zipfile для работы с ZIP-архивами
import os  # Импортирует модуль os для взаимодействия с операционной системой
import argparse  # Импортирует модуль argparse для парсинга аргументов командной строки
import csv  # Импортирует модуль csv для работы с CSV-файлами
import datetime  # Импортирует модуль datetime для работы с датами и временем
import tempfile  # Импортирует модуль tempfile для создания временных файлов и директорий

def extract_zip(zip_path, extract_to):
    """Извлекает ZIP-файл в указанную директорию."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:  # Открывает ZIP-файл для чтения
        zip_ref.extractall(extract_to)  # Извлекает все файлы в указанную директорию

def load_config(config_path):
    """Загружает конфигурацию из CSV-файла."""
    with open(config_path, newline='') as csvfile:  # Открывает CSV-файл для чтения
        reader = csv.reader(csvfile)  # Создает объект для чтения строк из CSV
        config = {row[0]: row[1] for row in reader}  # Создает словарь с конфигурацией
    return config  # Возвращает загруженную конфигурацию

def execute_command(command, cwd):
    """Выполняет команду в эмуляторе оболочки."""
    parts = command.split()  # Разделяет команду на части
    cmd = parts[0]  # Получает первую часть команды (имя команды)

    if cmd == 'ls':  # Если команда 'ls':
        return os.listdir(cwd)  # Возвращает список файлов и директорий в текущей директории
    elif cmd == 'cd':  # Если команда 'cd':
        if len(parts) > 1:  # Проверяет, указана ли директория
            new_dir = parts[1]  # Получает имя новой директории
            new_path = os.path.join(cwd, new_dir)  # Создает полный путь к новой директории.
            if os.path.isdir(new_path):  # Проверяет, существует ли директория
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
            os.makedirs(os.path.join(cwd, new_dir), exist_ok=True)  # Создает директорию
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

    