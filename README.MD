                                        Projec Notes_API

                                            1. Настройка приложения

В проекте используется Python 3.11.
Для управления зависимостями в проекте используется poetry. Если у вас не установлен poetry, то вам необходимо
открыть Powershell и прописать ссылку: для Windows (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -.
Для Linux, MacOS: curl -sSL https://install.python-poetry.org | python3 -
Для проверки успешной установки poetry, необходимо прописать команду poetry version.
Для того, чтобы добавить зависимости в наш проект, необходимо прописать команду poetry add, а для того, чтобы установить зависимости из
файла poetry.toml, необходимо прописать команду poetry install.
В качестве БД используется Postgresql 15. 
                                        
                                            2. Структура проекта

1. В основной директории проекта (notes_API) мы создали директорию backend, в которой и будут расположены все основные файлы для работы c
backend.
2. В директории api находятся эндпоинты (uesr.py,  note.py, home.py), а также файл api.py, который отвечает за роутеры.
3. В директории core находится файл конфигурации config.py нашего проекта, а также файл security.py, отвечающий за хэширование пароля
при регистрации нового пользователя.
4. В директории crud находятся файлы, в которых прописаны базовые операции, которые могут быть выполнены в нашем проекте.
5. В директории models размещены определения моделей данных, которые используются в приложении. 
Модели данных - это классы, которые определяют структуру данных и их отношения в базе данных.
6. В директории schemas описано определения схем данных, которые используются для валидации и сериализации данных в приложении. 
Схемы данных определяют формат и типы данных, которые должны содержаться в запросах и ответах API.
7. В директории db находятся файлы, связанные с базой данных. 

                                             3. Связь с БД и запуск приложения

Для того, чтобы метаданные попали в нашу БД, мы используем alembic. Для инициализации alembic в нашем проекте
мы должны прописать команду alembic init alembic. У нас появится директория alembic, а также файл alembic.ini.
В директории alembic находится файл env.py, в котором прописаны настройки.
После того, как мы настроили alembic, мы можем провести первую миграцию при помощи команды
alembic revision --autogenerate -m "Init db". Если все правильно настроено, то в нашей БД должны появится метаданные 
(наши таблицы: user, note, role).
Для добавления данных в наши таблицы, мы создали файл run_db.py в котором прописали скрипт для автоматического дабовления данных из
файла конфигурации.
Для запуска приложения мы создали основной файл main.py, в котором мы прописали все основные зависимости и маршруты.
Чтобы приложение запустилось, необходимо прописать команду: uvicorn main:app --reload

                                            

                                    



