# Проект курса [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/promo#toc)

---

Проект по автоматизации тестирования, разработанный в рамках курса [Stepik](https://stepik.org/course/575/promo#toc)  с использованием Selenium и паттерна Page Object Model

## Структура проекта

- `conftest.py` - файл конфигурации для инициализации драйвера
- `pages/` - директория с классами страниц (Page Object Model)
- `tests/` - директория с тестами


## Установка и настройка

1. Создайте виртуальное окружение:
   ```shell
   python -m venv venv && cd venv
   
2. Клонируйте репозиторий
   ```shell
   git clone https://github.com/MaksimPopovv/UI_tests.git && cd UI_tests

3. Установите зависимости из файла requirements.txt:
   ```shell
   pip install -r requirements.txt

4. Для запуска тестов используйте команду:
   ```shell
   pytest -v --tb=line
