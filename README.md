Task:
Установить Docker, собрать контейнер для webAdmin
Decision:
Для Запуска проекта необходимо ввести следующие команды:
docker compose down -v
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec -T postgres psql -U dato -d dato138it < backupDb.sql
Ссылка на страницу:
http://localhost:8000
http://localhost:8000/admin
Task:
улучшить существующий REST API;
добавить поиск и фильтрацию;
добавить пагинацию;
настроить Swagger.
Decision:
docker compose down
docker compose up --build
Ссылка на страницу:
http://localhost:8000/api/docs
http://localhost:8000/api/portfolio/?cat=1
http://localhost:8000/api/portfolio/?search=Python
http://localhost:8000/api/schema/swagger-ui/
Task:
Установим JWT-библиотеку.
Настроим settings.py.
Добавим URL для получения токена.
Получим первый JWT-токен.
Проверим защищенный API.
Decision:
docker compose build
docker compose up
Ссылка на страницу:
http://localhost:8000/api/token/
http://localhost:8000/api/portfolio/latest/
http://localhost:8000/api/portfolio/latest/?count=1
http://localhost:8000/api/portfolio/latest/?count=5
http://localhost:8000/api/portfolio/latest/?count=abc
http://localhost:8000/api/portfolio/latest/?count=-10
http://localhost:8000/api/portfolio/latest/?count=1000
http://localhost:8000/api/portfolio/1/info/
http://localhost:8000/api/portfolio/7/info/
http://localhost:8000/api/portfolio/5/duplicate/
Task:
✅ JWT (логин по токену)
✅ Permissions
✅ Загрузка файлов через API
✅ Права пользователей
✅ Пагинация и производительность
✅ Тестирование
✅ Деплой на VPS
Decision:
docker compose build
docker compose up
Ссылка на страницу:
http://localhost:8000/api/schema/swagger-ui
http://localhost:8000/api/docs
http://localhost:8000/api/portfolio/
Task:
Загрузка файлов через API (ImageField, FileField, multipart/form-data).
Права владельца объекта (только автор записи может её изменять или удалять).
Оптимизация запросов (select_related, prefetch_related).
Тестирование API (pytest, APIClient).
Развертывание проекта (Gunicorn + Nginx + Docker Compose на VPS).
Decision:
docker compose build
docker compose up
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
Ссылка на страницу:
http://localhost:8000/api/portfolio/
http://localhost:8000/media/uploads/2026/07/23/ChatGPT_Image_14_%D0%BC%D0%B0%D1%8F_2026_%D0%B3._09_36_04.png
http://localhost:8000/api/docs
Task:
Тестирование API (pytest, APIClient).
Decision:
docker compose build
docker compose up
docker compose exec web python manage.py test
docker compose exec web python manage.py test webApp
Task:
GitHub Actions.
💻 Локально — PostgreSQL (как сейчас).
🌐 На сервере — PostgreSQL.
🤖 GitHub Actions — SQLite только для тестов.
Decision:
- fileExecute.sh используется для предоставления прав доступа
- gitAdd.sh используется для добавления нового проекта в гитхаб
- gitDiff.sh Сравнивает изменения в гитхабе
- gitPush.sh Добавляет изменения в гитхаб
для запуска скрипта необходимо ввести команды:
cd scripts/
pwd
./fileExecute.sh
Введите путь к файлу: /home/dato/dato138it/scripts/gitAdd.sh
./gitAdd.sh
Enter GitHub repository URL: https://github.com/it38dato/webDato38it
Enter commit message: Config django, drf, docker, token, test
...
Username for 'https://github.com': it38dato
Password for 'https://it38dato@github.com':
...