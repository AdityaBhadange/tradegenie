from rest_framework import serializers
from .models import User, SellerProfile, Keyword, Product, Catagory,CategoryKeyword, DeliveryPartner, BuyerProfile, DeliveryPartnerOrder,Country, City, Tax, Notification, Group, CommissionGroup, Auth


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"