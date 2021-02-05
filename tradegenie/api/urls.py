from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("users", views.UserView)

urlpatterns = [
	# User url's
	path("users/", views.UserList.as_view()),
	path("users/<int:pk>/", views.UserDetail.as_view()),

	# groups url's
	path("groups/", views.GroupList.as_view()),
	path("groups/<int:pk>/", views.GroupDetail.as_view()),

	# catagory url's
	path("catagory/", views.CatagoryList.as_view()),
	path("catagory/<int:pk>/", views.CatagoryDetail.as_view()),

	# deliverypartner url's
	path("deliverypartners/", views.DeliveryPartnerList.as_view()),
	path("deliverypartners/<int:pk>/", views.DeliveryPartnerDetail.as_view()),

	# products url's
	path("products/", views.ProductList.as_view()),
	path("products/<int:pk>/", views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
