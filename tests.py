import unittest  # Импортирует модуль unittest для создания и выполнения тестов
from emulator import execute_command  # Импортирует функцию execute_command из модуля emulator

class TestShellEmulator(unittest.TestCase):
    """Класс для тестирования эмулятора оболочки, наследующий unittest.TestCase."""

    def setUp(self):
        """Инициализирует виртуальную файловую систему перед каждым тестом."""
        self.virtual_fs = {}  # Виртуальная файловая система как словарь
        self.cwd = '/'  # Текущая директория (корневая)

    def test_ls_empty_directory(self):
        """Тест команды 'ls' в пустой директории."""
        result = execute_command('ls', self.cwd, self.virtual_fs)  # Выполняет команду 'ls' в пустой виртуальной директории
        self.assertEqual(result, [], "Expected empty list for 'ls' in an empty directory")  # Проверяет, что результат - пустой список
        print("Test 'ls_empty_directory' passed.")  # Сообщает о прохождении теста

    def test_ls_with_files(self):
        """Тест команды 'ls' в директории с файлами."""
        test_dir = '/test_dir'  # Создает путь к новой виртуальной директории
        self.virtual_fs[test_dir + '/file.txt'] = b'Hello'  # Создает файл file.txt в виртуальной системе

        result = execute_command('ls', test_dir, self.virtual_fs)  # Выполняет команду 'ls' в директории с файлом
        self.assertEqual(result, [test_dir + '/file.txt'], "Expected file.txt in 'ls' result")  # Проверяет, что результат включает 'file.txt'
        print("Test 'ls_with_files' passed.")  # Сообщает о прохождении теста

    def test_cd_valid_directory(self):
        """Тест команды 'cd' в существующую директорию."""
        test_dir = '/test_dir'  # Определяет путь к новой виртуальной директории
        self.virtual_fs[test_dir] = None  # Создает новую виртуальную директорию
        result = execute_command(f'cd test_dir', self.cwd, self.virtual_fs)  # Выполняет команду 'cd' в созданную директорию
        self.assertEqual(result, test_dir, "Expected to change directory to test_dir")  # Проверяет, что результат соответствует пути новой директории
        print("Test 'cd_valid_directory' passed.")  # Сообщает о прохождении теста

    def test_cd_invalid_directory(self):
        """Тест команды 'cd' в несуществующую директорию."""
        result = execute_command('cd non_existing_dir', self.cwd, self.virtual_fs)  # Выполняет команду 'cd' в несуществующую директорию
        self.assertEqual(result, 'cd: non_existing_dir: No such file or directory', 
                         "Expected error message for non-existing directory")  # Проверяет, что возвращается сообщение об ошибке
        print("Test 'cd_invalid_directory' passed.")  # Сообщает о прохождении теста

    def test_mkdir_creates_directory(self):
        """Тест команды 'mkdir' для создания новой виртуальной директории."""
        result = execute_command('mkdir new_dir', self.cwd, self.virtual_fs)  # Выполняет команду 'mkdir' для создания директории
        self.assertEqual(result, 'Directory new_dir created', "Expected directory creation message")  # Проверяет, что возвращается сообщение о создании директории
        self.assertIn('/new_dir', self.virtual_fs, "Expected 'new_dir' to be created in virtual file system")  # Проверяет, что новая директория создана
        print("Test 'mkdir_creates_directory' passed.")  # Сообщает о прохождении теста

    def test_uname(self):
        """Тест команды 'uname'."""
        result = execute_command('uname', self.cwd, self.virtual_fs)  # Выполняет команду 'uname'
        self.assertEqual(result, 'Unix Emulated', "Expected 'Unix Emulated' from uname command")  # Проверяет, что результат соответствует ожидаемому
        print("Test 'uname' passed.")  # Сообщает о прохождении теста

    def test_date(self):
        """Тест команды 'date'."""
        result = execute_command('date', self.cwd, self.virtual_fs)  # Выполняет команду 'date'
        self.assertIsInstance(result, str, "Expected string from date command")  # Проверяет, что результат - строка
        print("Test 'date' passed.")  # Сообщает о прохождении теста

    def test_exit(self):
        """Тест команды 'exit'."""
        result = execute_command('exit', self.cwd, self.virtual_fs)  # Выполняет команду 'exit'
        self.assertEqual(result, 'Exiting', "Expected 'Exiting' message from exit command")  # Проверяет, что результат соответствует ожидаемому сообщению
        print("Test 'exit' passed.")  # Сообщает о прохождении теста

if __name__ == '__main__':
    unittest.main()  # Запускает выполнение тестов
