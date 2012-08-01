from tendenci.core.registry import site
from tendenci.core.registry.base import AppRegistry, lazy_reverse
from tendenci.apps.martins_products.models import Product


class ProductRegistry(AppRegistry):
    version = '1.0'
    author = 'Schipul - The Web Marketing Company'
    author_email = 'programmers@schipul.com'
    description = 'Create products type of content'

site.register(Product, ProductRegistry)