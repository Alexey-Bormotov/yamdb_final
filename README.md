# API для базы данных YaMDb

## 1. [Описание](#1)
## 2. [Установка Docker (на платформе Ubuntu)](#2)
## 3. [Переменные окружения](#3)
## 4. [Команды для запуска](#4)
## 5. [Заполнение базы данных](#5)
## 6. [Техническая информация](#6)
## 7. [Об авторе](#7)

---
## 1. Описание <a id=1></a>

Проект предназначен для взаимодействия с API социальной сети YaMDb.
YaMDb собирает отзывы пользователей на различные произведения.

API предоставляет возможность взаимодействовать с базой данных по следующим направлениям:
  - авторизироваться
  - создавать свои отзывы и управлять ими (корректировать\удалять)
  - просматривать и комментировать отзывы других пользователей
  - просматривать комментарии к своему и другим отзывам
  - просматривать произведения, категории и жанры произведений

---
## 2. Установка Docker (на платформе Ubuntu) <a id=2></a>

Проект поставляется в трёх контейнерах Docker (db, web, nginx).
Для запуска необходимо установить Docker и Docker Compose.

Подробнее об установке на других платформах можно узнать на [официальном сайте](https://docs.docker.com/engine/install/).

Для начала необходимо скачать и выполнить официальный скрипт:
```bash
apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

При необходимости удалить старые версии Docker:
```bash
apt remove docker docker-engine docker.io containerd runc 
```

Установить пакеты для работы через протокол https:
```bash
apt update
```
```bash
apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y 
```

Добавить ключ GPG для подтверждения подлинности в процессе установки:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Добавить репозиторий Docker в пакеты apt и обновить индекс пакетов:
```bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
```
```bash
apt update
```

Установить Docker(CE) и Docker Compose:
```bash
apt install docker-ce docker-compose -y
```

Проверить что  Docker работает можно командой:
```bash
systemctl status docker
```

Подробнее об установке можно узнать по [ссылке](https://docs.docker.com/engine/install/ubuntu/).

---
## 3. Переменные окружения <a id=3></a>

Проект использует базу данных PostgreSQL.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в папке "./infra/".

Шаблон для заполнения файла ".env":
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='Здесь указать секретный ключ'
```

---
## 4. Команды для запуска <a id=4></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/DIABLik666/yamdb_final.git
SSH: git clone git@github.com:DIABLik666/yamdb_final.git
```

Развернуть виртуальное окружение:
```bash
python -m venv venv
```

И установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Из папки "./infra/" выполнить команду создания и запуска контейнеров:
```bash
docker-compose up
```

После успешного запуска контейнеров выполнить миграции:
```bash
docker-compose exec web python manage.py migrate
```

Создать суперюзера:
```bash
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input 
```

Теперь доступность проекта можно проверить по адресу [http://localhost/admin/](http://localhost/admin/)

---
## 5. Заполнение базы данных <a id=5></a>

Скопировать файл с дампом базы данных из папки "./infra/" в контейнер:
```bash
docker cp fixtures.json infra_web_1:/app/fixtures.json
```

Заполнить базу данных из файла с дампом:
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

---
## 6. Техническая информация <a id=6></a>

Стек технологий: Python 3, Django, Django Rest, Docker, PostgreSQL, nginx, gunicorn, simple JWT.

Веб-сервер: nginx (контейнер nginx)  
Backend фреймворк: Django (контейнер web)  
API фреймворк: Django REST (контейнер web)  
База данных: PostgreSQL (контейнер db)

Веб-сервер nginx перенаправляет запросы клиентов к контейнеру web, либо к хранилищам (volume) статики и файлов.  
Контейнер nginx взаимодействует с контейнером web через gunicorn.

---
## 7. Об авторе <a id=7></a>

Бормотов Алексей Викторович  
Python-разработчик (Backend)  
Россия, г. Кемерово  
E-mail: di-devil@yandex.ru  
Telegram: @DIABLik666

### Соавторы:
- [UfoNexus](https://github.com/UfoNexus)  
- [ATIMSRU](https://github.com/ATIMSRU)
