from django.urls import path

from foods import views

urlpatterns = [
    path("foods/", views.FoodCategoryListView.as_view(), name="foods-categories")
]
