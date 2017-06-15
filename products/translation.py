from modeltranslation.translator import translator, TranslationOptions
from products.models import Category, Product, Industry

class CategorysTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategorysTranslationOptions)

class ProductsTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Product, ProductsTranslationOptions)

class IndustrysTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Industry, IndustrysTranslationOptions)
