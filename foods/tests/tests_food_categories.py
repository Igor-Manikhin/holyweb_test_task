from django.urls import reverse
from mixer.backend import django
from rest_framework import status
from rest_framework import test

from foods.tests import utils

FOODS_CATEGORIES_API_URL = reverse("foods-categories")

FOOD_CATEGORY_MOCK_INSTANCES_COUNT = 10
FOOD_MOCK_INSTANCES_COUNT = 2


class FoodCategoriesTests(test.APITestCase):
    """
    Тесты для проверки корректности работы API-ручки получения списка
    продуктов, агрегируемых по категориям
    """

    def test_food_categories_list_without_foods(self):
        utils._create_food_categories_mocks(count=FOOD_CATEGORY_MOCK_INSTANCES_COUNT)

        response = self.client.get(FOODS_CATEGORIES_API_URL)

        self.assertEqual(len(response.json()), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_food_categories_list_with_published_foods(self):
        categories = utils._create_food_categories_mocks(count=FOOD_CATEGORY_MOCK_INSTANCES_COUNT)
        utils._create_food_mocks(count=FOOD_MOCK_INSTANCES_COUNT, category=categories[0])
        utils._create_food_mocks(count=FOOD_MOCK_INSTANCES_COUNT, category=categories[1])

        response = self.client.get(FOODS_CATEGORIES_API_URL)

        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_food_categories_list_with_non_published_foods(self):
        utils._create_food_categories_mocks(count=FOOD_CATEGORY_MOCK_INSTANCES_COUNT)
        utils._create_food_mocks(count=FOOD_MOCK_INSTANCES_COUNT, category=django.mixer.SELECT, is_publish=False)

        response = self.client.get(FOODS_CATEGORIES_API_URL)

        self.assertEqual(len(response.json()), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_food_categories_list_with_non_published_and_published_foods(self):
        categories = utils._create_food_categories_mocks(count=FOOD_CATEGORY_MOCK_INSTANCES_COUNT)
        utils._create_food_mocks(count=FOOD_MOCK_INSTANCES_COUNT, category=categories[0])
        utils._create_food_mocks(count=FOOD_MOCK_INSTANCES_COUNT, category=django.mixer.SELECT, is_publish=False)

        response = self.client.get(FOODS_CATEGORIES_API_URL)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
