# Шаги запуска backend-севера
1) Перейти в папку src/poetry и установить зависимости:

    poetry install

2) Скачать image postgres:

    sudo docker pull postgres

3) Создать контейнер docker: 

    sudo docker run --rm --name product -e POSTGRES_PASSWORD=qwerfdsa -e POSTGRES_USER=yngcrovi -e POSTGRES_DB=product -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

4) Запустить контейнер:

    sudo docker run product

5) Запустить docker-compose файл:

    sudo docker compose up -d

6) Перейти в папку src и запустить сервер:

    uvicorn main:app --reload --port 8000