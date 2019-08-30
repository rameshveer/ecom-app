from django.urls import path

from item_api import views


urlpatterns = [
    path('item/', views.ItemApiView.as_view()),
]
