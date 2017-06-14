from modeltranslation.translator import translator, TranslationOptions
from products.models import Category

class CategorysTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategorysTranslationOptions)