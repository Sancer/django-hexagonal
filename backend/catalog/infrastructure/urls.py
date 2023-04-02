from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('product/', views.SearchProductView.as_view(), name="search"),
]