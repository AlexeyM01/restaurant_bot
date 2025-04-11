# Restaurant Bot

## Назначение проекта
Телеграм чат-бот для бронирования столиков в ресторане

## Системные требования

- **Язык программирования**: Python 3.9 или выше
- **База данных**: MySQL
- **Docker**: версия 20.10.0 или выше (для контейнеризации приложения)
- **Docker Compose**: версия 1.27.0 или выше

### Системные зависимости

- **Python библиотеки**:
  - aiogram
  - aiogram_calendar
  - aiogram_dialog
  - sqlalchemy
  - pydantic
  - python-dotenv

## Шаги по установке, сборке и запуску

### 1. Клонирование репозитория

Клонируйте репозиторий на свою локальную машину:

```bash
git clone https://github.com/AlexeyM01/restaurant_bot
cd restaurant_bot
```

### 2. Установка Docker и Docker Compose
Убедитесь, что Docker и Docker Compose установлены на вашем компьютере. Инструкции по установке [Docker](https://docs.docker.com/get-started/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/).

### 3. Настройка переменных окружения
Создайте файл .env в корневой директории проекта и добавьте необходимые переменные окружения:

```text
DB_HOST=db
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASS=your_password
TELEGRAM_TOKEN=your_telegram_bot_token
```

### 4. Сборка и запуск контейнеров
Запустите следующую команду для сборки и запуска контейнеров:

```bash
docker-compose up --build
```
