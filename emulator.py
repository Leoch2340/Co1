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
