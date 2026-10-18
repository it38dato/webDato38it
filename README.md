# webDato38it

Backend-проект на Python/Django, который я использую для практики разработки веб-приложений, REST API, работы с PostgreSQL, Docker, CI/CD и внешними интеграциями.

Проект постепенно развивается: от обычного Django-приложения до полноценного backend-стека с REST API, авторизацией, тестированием, production-конфигурацией и интеграцией с ботом.

## 🚀 Что реализовано

* Django + Django REST Framework
* PostgreSQL
* REST API
* JWT-аутентификация
* Permissions и права пользователей
* Загрузка файлов через API
* Поиск, фильтрация и пагинация
* Swagger / OpenAPI
* Тестирование API
* Docker / Docker Compose
* Gunicorn
* Nginx
* GitHub Actions
* Production-конфигурация
* Интеграция с ботом MAX

## 🤖 MAX Bot

В рамках дальнейшего развития проекта добавлена интеграция с ботом MAX.

Сейчас бот находится на этапе тестирования.

Основная задача интеграции — обеспечить взаимодействие бота с backend-приложением и постепенно расширять его функциональность.

## 🛠 Стек

**Backend:**

* Python
* Django
* Django REST Framework

**Database:**

* PostgreSQL

**API:**

* REST API
* JWT
* Swagger / OpenAPI

**DevOps:**

* Docker
* Docker Compose
* Nginx
* Gunicorn
* GitHub Actions

**Testing:**

* Django Test Framework
* APIClient
* pytest

## 📁 Структура проекта

```text
webDato38it/
├── dato138it/       # настройки Django
├── webApp/          # основное приложение
├── max_bot/         # интеграция с MAX
├── nginx/           # конфигурация Nginx
├── scripts/         # вспомогательные скрипты
├── static/
├── staticfiles/
├── media/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
└── requirements.txt
```

## ▶️ Запуск

Клонировать репозиторий:

```bash
git clone https://github.com/it38dato/webDato38it.git
cd webDato38it
```

Запустить Docker Compose:

```bash
docker compose up --build
```

Применить миграции:

```bash
docker compose exec web python manage.py migrate
```

Создать администратора:

```bash
docker compose exec web python manage.py createsuperuser
```

После запуска:

```text
http://localhost:8000
http://localhost:8000/admin
http://localhost:8000/api/docs
```

## 🧪 Тестирование

Запуск тестов:

```bash
docker compose exec web python manage.py test
```

Также тестируется REST API с использованием APIClient.

## 📌 Текущий статус

Проект находится в активной разработке.

Сейчас основное направление работы — развитие интеграции с MAX Bot, тестирование взаимодействия с backend и дальнейшее улучшение архитектуры проекта.

## 🎯 Цель проекта

Проект создаётся как практическая площадка для развития навыков Python Backend Development.

В процессе разработки я практикую:

* разработку REST API;
* работу с PostgreSQL;
* Docker-контейнеризацию;
* аутентификацию и авторизацию;
* тестирование;
* CI/CD;
* настройку production-окружения;
* интеграцию внешних сервисов;
* разработку и поддержку backend-приложения.

## 🔗 Автор

GitHub: https://github.com/it38dato
