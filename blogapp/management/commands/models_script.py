from django.core.management.base import BaseCommand
from blogapp.models import Category, Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))
        print('End')

        post = Post.objects.first()
        print(post.name)
        print(post.text)

        category = post.category
        print(category.name)
        print(type(category))