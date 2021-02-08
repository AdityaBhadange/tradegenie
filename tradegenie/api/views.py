from django.shortcuts import render
# from rest_framework import viewsets
from .models import (User, Group, Catagory, DeliveryPartner,
					Product, Keyword, Order, DeliveryPartnerOrder,
					SellerProfile, BuyerProfile)

from .serializers import (UserSerializer, GroupSerializer, CatagorySerializer, 
						DeliveryPartnerSerializer, ProductSerializer, KeywordSerializer, 
						OrderSerializer, DeliveryPartnerOrderSerializer, SellerProfileSerializer,
						BuyerProfileSerializer)

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


# Catagory view
class CatagoryList(generics.ListCreateAPIView):
	queryset = Catagory.objects.all()
	serializer_class = CatagorySerializer


class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Catagory.objects.all()
	serializer_class = CatagorySerializer


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