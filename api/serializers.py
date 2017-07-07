from rest_framework import serializers
from products.models import Product, Category

class ProductSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(
    #     max_length=50, required=False, allow_null=True, allow_blank=True)
    # category_id = serializers.IntegerField()
    class Meta:
      model = Product
      # exclude = ('create_at', 'name_vi', 'name_en')
      fields = ('name', 'category_id')

