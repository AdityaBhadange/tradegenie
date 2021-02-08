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

	# deliverypartner url's
	path("deliverypartners/", views.DeliveryPartnerList.as_view()),
	path("deliverypartners/<int:pk>/", views.DeliveryPartnerDetail.as_view()),

	# products url's
	path("products/", views.ProductList.as_view()),
	path("products/<int:pk>/", views.ProductDetail.as_view()),

	# client url's
	path('client/', views.ClientList.as_view()),
	path('client/<int:pk>/', views.ClientDetail.as_view()),

	# keyword url's
	path("keywords/", views.KeywordList.as_view()),
	path("keywords/<int:pk>/", views.KeywordDetail.as_view()),

	# order url's
	path("orders/", views.OrderList.as_view()),
	path("orders/<int:pk>/", views.OrderDetail.as_view()),

	# deliver partner order url's
	path("deliveryorders/", views.DeliveryPartnerOrderList.as_view()),
	path("deliveryorders/<int:pk>/", views.DeliveryPartnerOrderDetail.as_view()),

	# BuyerProfile url's
    path("buyerprofile/", views.BuyerProfileList.as_view()),
    path("buyerprofile/<int:pk>/", views.BuyerProfileDetail.as_view()),

    # SellerProfile url's
    path("sellerprofile/", views.SellerProfileList.as_view()),
    path("sellerprofile/<int:pk>/", views.SellerProfileDetail.as_view()),

    # catagory url's
    path("catagory/", views.CatagoryList.as_view()),
    path("catagory/<int:pk>/", views.CatagoryDetail.as_view()),

    # CategoryKeyword url's
    path("categorykeyword/", views.CategoryKeywordList.as_view()),
    path("categorykeyword/<int:pk>/", views.CategoryKeywordDetail.as_view()),

    # city url
    path('city/',views.CityList.as_view()),
    path('city/<int:pk>/',views.CityDetail.as_view()),

    # tax url
    path('tax/',views.TaxList.as_view()),
    path('tax/<int:pk>/',views.TaxDetail.as_view()),

    # product url
    path('product/', views.ProducttList.as_view()),
	path('product/<int:pk>/', views.ProductDetail.as_view()),

	# product keyword url
	path('productkeyword/', views.ProductkeywordtList.as_view()),
	path('productkeyword/<int:pk>/', views.ProductKeywordDetail.as_view()),

	# notification url
	path('notification/', views.NotificationList.as_view()),
	path('notification/<int:pk>/', views.NotificationDetail.as_view()),

	# userinterest url
	path('userinterest/', views.UserInterestList.as_view()),
	path('userinterest/<int:pk>/', views.UserInterestDetail.as_view()),

	# auth url's
    path('auth/', views.AuthList.as_view()),
    path('auth/<int:pk>', views.AuthDetail.as_view()),

    # groupcommission url's
    path('groupcommission/', views.ComissionGroupList.as_view()),
    path('groupcomission/<int:pk>', views.ComissionGroupDetail.as_view()),

    # country url's
    path('country/', views.CountryList.as_view()),
    path('country/<int:pk>', views.CountryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
