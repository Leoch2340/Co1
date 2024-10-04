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

    def test_ls_with_files(self):
        """Тест команды 'ls' в директории с файлами."""
        test_dir = os.path.join(self.temp_dir, 'test_dir')  # Определяет путь к новой директории
        os.makedirs(test_dir)  # Создает новую директорию

        with open(os.path.join(test_dir, 'file.txt'), 'w') as f:  # Создает файл file.txt в новой директории
            f.write('Hello')  # Записывает 'Hello' в файл

        result = execute_command('ls', test_dir)  # Выполняет команду 'ls' в директории с файлом
        self.assertEqual(result, ['file.txt'], "Expected file.txt in 'ls' result")  # Проверяет, что результат включает 'file.txt'
        print("Test 'ls_with_files' passed.")  # Сообщает о прохождении теста