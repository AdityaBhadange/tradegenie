from django.shortcuts import render
# from rest_framework import viewsets
from .models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework import mixins
from rest_framework import generics


class UserList(mixins.ListModelMixin,
			mixins.CreateModelMixin,
			generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin,
				mixins.UpdateModelMixin,
				mixins.DestroyModelMixin,
				generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class GroupList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class GroupDetail(mixins.RetrieveModelMixin,
				mixins.UpdateModelMixin,
				mixins.DestroyModelMixin,
				generics.GenericAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)