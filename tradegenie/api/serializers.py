from rest_framework import serializers
from .models import User, SellerProfile, Keyword, Product, Catagory,CategoryKeyword, DeliveryPartner, BuyerProfile, DeliveryPartnerOrder,Country, City, Tax, Notification, Group, CommissionGroup, Auth


# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


# Group Serializer
class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"


# Catagory Serializer
class CatagorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Catagory
		fields = "__all__"


# DeliveryPartner Serializer
class DeliveryPartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeliveryPartner
		fields = "__all__"


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"
