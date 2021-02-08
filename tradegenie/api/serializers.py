from rest_framework import serializers
from .models import (User, SellerProfile, Keyword, Product, 
					Catagory, CategoryKeyword, DeliveryPartner, 
					BuyerProfile, DeliveryPartnerOrder, Country, 
					City, Tax, Notification, Group, 
					CommissionGroup, Auth, Order, Client, 
					ProductKeyword)


# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


# Keyword Serializer
class KeywordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Keyword
		fields = "__all__"


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = "__all__"


# DeliveryPartnerOrder Serializer
class DeliveryPartnerOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeliveryPartnerOrder
		fields = "__all__"


# BuyerProfile Serializer
class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerProfile
        fields = "__all__"


# SellerProfile Serializer
class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = "__all__"


# Catagory Serializer
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = "__all__"


# CategoryKeyword Serializer
class CategoryKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryKeyword
        fields = "__all__"


# City Serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City

        fields = '__all__'


# Tax Serialzier
class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'


# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Group Serializer
class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
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


# ProductKeyword Serializer
class ProductkeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductKeyword
        fields = '__all__'


# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'