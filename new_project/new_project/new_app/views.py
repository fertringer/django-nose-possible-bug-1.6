from models import Category


def view_category():
    return Category.objects.get_or_create(name='Null')
