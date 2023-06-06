from django.db.models import Exists
from django.db.models import OuterRef
from django.db.models import Prefetch
from rest_framework import generics

from foods import models
from foods import serializers


def _get_food_categories_queryset():
    prefetch_foods_subquery = models.Food.objects.filter(is_publish=True).all()
    exists_foods_subquery = Exists(
        models.Food.objects.filter(is_publish=True, category=OuterRef('pk')).all()
    )

    return models.FoodCategory.objects.prefetch_related(
        Prefetch("food", queryset=prefetch_foods_subquery), "food__additional",
    ).annotate(foods_exist=exists_foods_subquery).filter(foods_exist=True).order_by().all()


class FoodCategoryListView(generics.ListAPIView):
    queryset = _get_food_categories_queryset()
    serializer_class = serializers.FoodListSerializer
