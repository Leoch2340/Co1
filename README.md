https://github.com/Leoch2340/Co1

1. Общее описание:
&nbsp;&nbsp;&nbsp;&nbsp; <br/> В рамках этого задания необходимо разработать эмулятор командной оболочки, который будет поддерживать выполнение базовых команд, таких как ls, cd, mkdir, uname, date, и exit. Помимо этого, требуется создать набор автоматических тестов, которые проверяют корректность работы каждой из этих команд. Эмулятор должен уметь взаимодействовать с файловой системой через временные директории и обрабатывать команды так, как если бы они выполнялись в реальной командной оболочке.

2. Описание всех функций и настроек: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Функции эмулятора оболочки: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;2.1 extract_zip(zip_path, extract_to)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Функция извлекает содержимое ZIP-архива в указанную директорию<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2.2 load_config(config_path)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Загружает настройки из CSV-файла конфигурации и возвращает их в виде словаря<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2.3 execute_command(command, cwd)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выполняет команду в эмуляторе оболочки и возвращает результат выполнения<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2.4 main()<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Основная функция эмулятора оболочки. Загружает конфигурацию, распаковывает виртуальную файловую систему, выполняет начальные команды и запускает интерактивный режим.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Настройки в CSV-файле:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;CSV-файл используется для задания конфигурации эмулятора. Он содержит следующие настройки:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username: Имя пользователя, которое будет отображаться в командной строке (например, user).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vfs: Путь к ZIP-файлу с виртуальной файловой системой (например, vfs.zip).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startscript: Путь к файлу начального сценария, который будет выполнен при старте эмулятора (например, start.sh).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Основные тесты:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_ls_empty_directory: Проверяет работу команды ls в пустой директории.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_ls_with_files: Проверяет работу команды ls в директории, содержащей файлы.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_cd_valid_directory: Проверяет команду cd, когда указывается существующая директория.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_cd_invalid_directory: Проверяет команду cd, когда указывается несуществующая директория.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_mkdir_creates_directory: Проверяет создание новой директории с помощью команды mkdir.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_uname: Проверяет работу команды uname, которая должна возвращать строку "Unix Emulated".<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_date: Проверяет корректность работы команды date.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_exit: Проверяет работу команды exit, которая завершает сессию.<br/>
3. Описание команд для сборки проекта:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Запуск эмулятора - python emulator.py config.csv<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Запуск тестов - python -m unittest tests.py<br/>
4. Примеры использования в виде скриншотов, желательно в анимированном/видео формате, доступном для web-просмотра:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/629925da-e5ee-4b9e-9f2d-9734122af90a)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;python emulator.py config.csv<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/60c6501c-94f9-489a-895f-c587d0e7c174)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;ls<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/4b4390cd-145d-4914-a0d0-99a94115702c)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;cd<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/c1b19f40-bc4b-43a7-9f90-fc13ba5919b6)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;mkdir<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/7383a667-88e5-4a9a-b83d-3d309fad5ed0)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;uname<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/c8061802-9a2c-4701-89f8-8fdd5e8cac4d)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;date<br/>

&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/2e457672-525e-4afc-a483-fef593ee6b98)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;exit<br/>
5. Результаты прогона тестов: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/bfc6bf8a-d31c-4109-9a17-6da6f6519981)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;python -m unittest tests.py  <br/>
