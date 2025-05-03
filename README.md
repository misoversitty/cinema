cinema

course-project on the discipline 'Software Solutions Development'

# How to run
## 1. Установить пакет и его зависимости.
```commandline
    make install
```
## 2. В файле `config` обновить параметр `ROOT_PATH`.
## 3. Создать в корневой папке приложения файл `secrets` следующего содержания.
```
[secrets]
DB_NAME = 
DB_SCHEMA = 
DB_USERNAME = 
DB_PASSWORD = 
DB_URI = 
```
## 4*. Восстановить базу из дампа.