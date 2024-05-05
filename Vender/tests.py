from django.test import TestCase
from django.urls import reverse
from .models import Vender
from .serializers import Venderserialiazer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ModelTests(TestCase):
    def test_vendor_creation(self):
        vendor = Vender.objects.create(
            name="Test Vendor",
            contact_details="Contact",
            address="Address",
            vendor_code="123",
            on_time_delivery_rate=95.0,
            quality_rating_avg=4.5,
            average_response_time=24.0,
            fulfillment_rate=98.0,
        )
        self.assertEqual(str(vendor), "Test Vendor")


# class ViewTests(TestCase):
#     def test_vendor_list_view(self):
#         url = reverse("vendors-list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class ViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

    def test_vendor_list_view(self):
        url = reverse("vendors-list")

        # Set token in request headers
        self.client.force_authenticate(user=self.user, token=self.token)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SerializerTests(TestCase):
    def test_vendor_serializer(self):
        data = {
            "name": "Test Vendor",
            "contact_details": "Contact",
            "address": "Address",
            "vendor_code": "123",
            "on_time_delivery_rate": 95.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 24.0,
            "fulfillment_rate": 98.0,
        }
        serializer = Venderserialiazer(data=data)
        self.assertTrue(serializer.is_valid())


class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

    def test_vendor_performance_api(self):
        vendor = Vender.objects.create(
            name="Test Vendor",
            contact_details="Contact",
            address="Address",
            vendor_code="123",
            on_time_delivery_rate=95.0,
            quality_rating_avg=4.5,
            average_response_time=24.0,
            fulfillment_rate=98.0,
        )
        url = reverse("VendorPerformanceAPIView", kwargs={"pk": vendor.pk})
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
