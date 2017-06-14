from rest_framework import serializers
from products.models import Product, Category

class ProductSerializers(serializers.ModelSerializer):
	# name = serializers.CharField(max_length=200)
	class Meta:
		model = Product
		# fields = '__all__'
		exclude = ('create_at',)

