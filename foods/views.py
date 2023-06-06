from django.db.models import Exists
from django.db.models import OuterRef
from django.db.models import Prefetch
from django.db.models import QuerySet
from rest_framework import generics

from foods import models
from foods import serializers


def _get_food_categories_queryset() -> QuerySet[models.FoodCategory]:
    prefetch_foods_subquery = models.Food.objects.filter(is_publish=True).all()
    exists_foods_subquery = Exists(
        models.Food.objects.filter(is_publish=True, category=OuterRef("pk")).all()
    )

    return models.FoodCategory.objects.prefetch_related(
        Prefetch("food", queryset=prefetch_foods_subquery), "food__additional",
    ).filter(exists_foods_subquery).order_by().all()


class FoodCategoryListView(generics.ListAPIView):
    """
    Представление для получения списка категорий с относимыми
    к ним продуктами
    """
    queryset = _get_food_categories_queryset()
    serializer_class = serializers.FoodListSerializer
