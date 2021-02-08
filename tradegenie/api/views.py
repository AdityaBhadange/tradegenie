from django.shortcuts import render
# from rest_framework import viewsets
from .models import (User, Group, Category, DeliveryPartner,
					Product, Keyword, Order, DeliveryPartnerOrder,
					SellerProfile, BuyerProfile, CategoryKeyword, City, Tax, 
					ProductKeyword, Notification, UserInterest, CommissionGroup,
					Auth, Country, Client)

from .serializers import (UserSerializer, GroupSerializer, CategorySerializer, 
						DeliveryPartnerSerializer, ProductSerializer, KeywordSerializer, 
						OrderSerializer, DeliveryPartnerOrderSerializer, SellerProfileSerializer,
						BuyerProfileSerializer, CategoryKeywordSerializer, CitySerializer,
						TaxSerializer, NotificationSerializer, UserInterestSerializer, 
                        AuthSerializer, CommissionGroupSerializer, CountrySerializer, 
                        ProductKeywordSerializer, ClientSerializer)

from rest_framework import mixins
from rest_framework import generics


# User view
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


# Group view
class GroupList(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


# DeliveryPartner view
class DeliveryPartnerList(generics.ListCreateAPIView):
	queryset = DeliveryPartner.objects.all()
	serializer_class = DeliveryPartnerSerializer


class DeliveryPartnerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DeliveryPartner.objects.all()
	serializer_class = DeliveryPartnerSerializer


# Product view
class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


# Keyword view
class KeywordList(generics.ListCreateAPIView):
	queryset = Keyword.objects.all()
	serializer_class = KeywordSerializer


class KeywordDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Keyword.objects.all()
	serializer_class = KeywordSerializer


# Order view
class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


# DeliveryPartnerOrder view
class DeliveryPartnerOrderList(generics.ListCreateAPIView):
	queryset = DeliveryPartnerOrder.objects.all()
	serializer_class = DeliveryPartnerOrderSerializer


class DeliveryPartnerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DeliveryPartnerOrder.objects.all()
	serializer_class = DeliveryPartnerOrderSerializer


# BuyerProfile view
class BuyerProfileList(generics.ListCreateAPIView):
    queryset = BuyerProfile.objects.all()
    serializer_class = BuyerProfileSerializer


class BuyerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuyerProfile.objects.all()
    serializer_class = BuyerProfileSerializer


# SellerProfile view
class SellerProfileList(generics.ListCreateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer


class SellerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer


# Category view
class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


# CategoryKeyword view
class CategoryKeywordList(generics.ListCreateAPIView):
    queryset = CategoryKeyword.objects.all()
    serializer_class = CategoryKeywordSerializer


class CategoryKeywordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryKeyword.objects.all()
    serializer_class = CategoryKeywordSerializer


# City view
class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# Tax view
class TaxList(generics.ListCreateAPIView):
   queryset = Tax.objects.all()
   serializer_class = TaxSerializer

class TaxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer


# ProductKeyword view
class ProductKeywordtList(generics.ListCreateAPIView):
    queryset = ProductKeyword.objects.all()
    serializer_class = ProductKeywordSerializer


class ProductKeywordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductKeyword.objects.all()
    serializer_class = ProductKeywordSerializer

# Client view
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Client.objects.all()
    serializer_class = ClientSerializer


# Notification view
class NotificationList(generics.ListCreateAPIView):
   queryset = Notification.objects.all()
   serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


# UserInterest view
class UserInterestList(generics.ListCreateAPIView):
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer


class UserInterestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =UserInterest.objects.all()
    serializer_class = UserInterestSerializer


# Comission view
class ComissionGroupList(generics.ListCreateAPIView):
    queryset = CommissionGroup.objects.all()
    serializer_class = CommissionGroupSerializer


class ComissionGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommissionGroup.objects.all()
    serializer_class = CommissionGroupSerializer


# Auth view
class AuthList(generics.ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer


class AuthDetail(generics.RetrieveUpdateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer


# Country view
class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
