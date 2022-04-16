import csv

from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


class Command(BaseCommand):
    help = 'Импорт всех данных из csv в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='Путь к файлу')

    def handle(self, *args, **options):
        print('Заполнение модели User из csv.')
        file_path = options['path'] + 'users.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                User.objects.create(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6]
                )
        print('Заполнение модели User прошло успешно.')
        print('----------')

        print('Заполнение модели Category из csv.')
        file_path = options['path'] + 'category.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                Category.objects.create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )
        print('Заполнение модели Category прошло успешно.')
        print('----------')

        print('Заполнение модели Genre из csv.')
        file_path = options['path'] + 'genre.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                Genre.objects.create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )
        print('Заполнение модели Genre прошло успешно.')
        print('----------')

        print('Заполнение модели Title из csv.')
        file_path = options['path'] + 'titles.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                category = Category.objects.get(pk=row[3])
                Title.objects.create(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=category,
                )
        print('Заполнение модели Title прошло успешно.')
        print('----------')

        print('Заполнение модели GenreTitle из csv.')
        file_path = options['path'] + 'genre_title.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                genre = Genre.objects.get(pk=row[2])
                title = Title.objects.get(pk=row[1])
                GenreTitle.objects.create(
                    id=row[0],
                    genre=genre,
                    title=title,
                )
        print('Заполнение модели GenreTitle прошло успешно.')
        print('----------')

        print('Заполнение модели Review из csv.')
        file_path = options['path'] + 'review.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                title = Title.objects.get(pk=row[1])
                author = User.objects.get(pk=row[3])
                Review.objects.create(
                    id=row[0],
                    title=title,
                    text=row[2],
                    author=author,
                    score=row[4],
                    pub_date=row[5],
                )
        print('Заполнение модели Review прошло успешно.')
        print('----------')

        print('Заполнение модели Comment из csv.')
        file_path = options['path'] + 'comments.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                review = Review.objects.get(pk=row[1])
                author = User.objects.get(pk=row[3])
                Comment.objects.create(
                    id=row[0],
                    review=review,
                    text=row[2],
                    author=author,
                    pub_date=row[4],
                )
        print('Заполнение модели Comment прошло успешно.')
        print('----------')
        print('Все модели заполнены успешно!')
