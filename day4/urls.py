from django.urls import path

from day4 import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<str:id>/", views.BookAPIView.as_view()),

    path("gen/", views.BookGenericAPIView.as_view()),
    path("gen/<str:id>/", views.BookGenericAPIView.as_view()),

    path("v2/gen/", views.BookGenericAPIViewV2.as_view()),
    path("v2/gen/<str:id>/", views.BookGenericAPIViewV2.as_view()),

    path("set/", views.UserAPIView.as_view({"post": "user_login", "get": "get_user_count"})),
    path("set/<str:id>/", views.UserAPIView.as_view({"post": "user_login", "get": "get_user_count"})),

    path("v2/set/", views.UserGenericViewSet.as_view({"get": "user_list"}))
]
