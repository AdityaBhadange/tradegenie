from django.shortcuts import render
# from rest_framework import viewsets
from .models import User, Group, Catagory, DeliveryPartner, Product
from .serializers import UserSerializer, GroupSerializer, CatagorySerializer, DeliveryPartnerSerializer, ProductSerializer
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
