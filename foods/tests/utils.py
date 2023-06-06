import decimal

from mixer.backend import django

from foods import models

FOOD_CATEGORY_MOCK_INSTANCE_NAME_FORMAT = "test_category_{0}"
FOOD_MOCK_INSTANCE_NAME_FORMAT = "test_food_{0}"
FOOD_MOCK_INSTANCE_COST = decimal.Decimal("200.00")


def _create_food_categories_mocks(
    count: int
) -> list[models.FoodCategory] | models.FoodCategory:
    mixer = django.mixer

    if count > 1:
        mixer = mixer.cycle(count)

    return mixer.blend(
        models.FoodCategory,
        name_ru=django.mixer.sequence(FOOD_CATEGORY_MOCK_INSTANCE_NAME_FORMAT),
    )


def _create_food_mocks(
    count: int,
    category: models.FoodCategory,
    is_publish: bool = True,
) -> list[models.Food] | models.Food:
    mixer = django.mixer

    if count > 1:
        mixer = mixer.cycle(count)

    return mixer.blend(
        models.Food,
        category=category,
        name_ru=django.mixer.sequence(FOOD_MOCK_INSTANCE_NAME_FORMAT),
        cost=FOOD_MOCK_INSTANCE_COST,
        is_publish=is_publish,
    )
