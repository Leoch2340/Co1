import unittest  # Импортирует модуль unittest для создания и выполнения тестов
import os  # Импортирует модуль os для взаимодействия с операционной системой
import tempfile  # Импортирует модуль tempfile для работы с временными файлами и директориями
from emulator import execute_command  # Импортирует функцию execute_command из модуля emulator
import shutil  # Импортирует модуль shutil для работы с файлами и директориями

class TestShellEmulator(unittest.TestCase):
    """Класс для тестирования эмулятора оболочки, наследующий unittest.TestCase."""

    def setUp(self):
        """Создает временную директорию для тестирования."""
        self.temp_dir = tempfile.mkdtemp()  # Создает временную директорию и сохраняет ее путь в атрибуте класса

    def tearDown(self):
        """Удаляет временную директорию после тестов."""
        shutil.rmtree(self.temp_dir)  # Удаляет временную директорию и все ее содержимое

    def test_ls_empty_directory(self):
        """Тест команды 'ls' в пустой директории."""
        result = execute_command('ls', self.temp_dir)  # Выполняет команду 'ls' в пустой временной директории
        self.assertEqual(result, [], "Expected empty list for 'ls' in an empty directory")  # Проверяет, что результат - пустой список
        print("Test 'ls_empty_directory' passed.")  # Сообщает о прохождении теста
