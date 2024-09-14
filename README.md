# Шаги запуска backend-севера
1) Забилдить docker-compose файл:

    - sudo docker compose build

2) Запустить контейнеры fastapi и postgres:

    - sudo docker compose up -d

- Контейнер fastapi должен находится на 8000 порту, а postgres 5432

3) Если по какой-то причине зависимости не установились, перейти в папку src/poetry и установить зависимости:

    - poetry install
    - poetry update

4) Перейти в файл create_table.py, который находится по маршруту src/repository и запустить его отдельно для создания таблиц

5) Для тестового задания я не стал добавлять .env файл в gitignor и создавать .env.example

5) Перейти в папку src и запустить сервер:

    - uvicorn main:app --reload --port 8000