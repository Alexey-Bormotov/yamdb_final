![yamdb workflow](https://github.com/DIABLik666/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект «api_yamdb» в контейнерах

## 1. [Описание](#1)
## 2. [Установка Docker](#2)
## 3. [Переменные окружения](#3)
## 4. [Команды для запуска](#4)
## 5. [Заполнение базы данных](#5)

---
## 1. Описание <a id=1></a>

Проект предназначен для взаимодействия с API социальной сети YaMDb.
YaMDb собирает отзывы пользователей на различные произведения.

API предоставляет возможность взаимодействовать с социальной сетью по следующим направлениям:
  - авторизироваться
  - создавать свои отзывы и управлять ими (корректировать\удалять)
  - просматривать и комментировать отзывы других пользователей
  - просматривать комментарии к своему и другим отзывам
  - просматривать произведения, категории и жанры произведений

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:DIABLik666/infra_sp2.git
```
---
## 2. Установка Docker <a id=2></a>

Проект поставляется в трёх контейнерах Docker (db, web, nginx).
Для запуска необходимо установить Docker и Docker Compose.

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

Шаблон для заполнения файла "./infra/.env":
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='KEY'
```

---
## 4. Команды для запуска <a id=4></a>

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
