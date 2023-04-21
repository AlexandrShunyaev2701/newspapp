from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удалять все новости из какой-либо категории'

    def add_arguments(self, parser):
        parser.add_argument('categories_name', type=str)

    def handle(self, *args, **options):
        categories_name = options['categories_name']
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить все новости данной категории? yes/no')
        answer = input()
        if answer == 'yes':
            post = Post.objects.filter(category__name_category=categories_name)
            post.delete()
            self.stdout.write('Вы удалили все новости данной категории')
