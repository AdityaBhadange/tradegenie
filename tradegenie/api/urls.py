from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("users", views.UserView)

urlpatterns = [
	# path("", include(router.urls))
	path("users/", views.UserList.as_view()),
	path("users/<int:pk>/", views.UserDetail.as_view()),
	path("groups/", views.GroupList.as_view()),
	path("groups/<int:pk>/", views.GroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
