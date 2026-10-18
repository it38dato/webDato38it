from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Portfolio
class PortfolioTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username="test",
			password="Ntcn"
		)
		Portfolio.objects.create(
			location="Tele2",
			specialization="Python Developer",
			responsibilities="Backend",
			progress="REST API",
		)
	def test_get_portfolio_list(self):
		url = reverse("portfolio-list")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["count"], 1)
	def test_create_portfolio(self):
		self.client.force_authenticate(user=self.user)
		url = reverse("portfolio-list")
		data = {
			"location": "Google",
			"specialization": "Python Developer",
			"responsibilities": "REST API",
			"progress": "Created project",
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Portfolio.objects.count(), 2)
	def test_create_portfolio_unauthorized(self):
	    url = reverse("portfolio-list")
	    data = {
	        "location": "Google",
	        "specialization": "Python Developer",
	        "responsibilities": "REST API",
	        "progress": "Created project",
	    }
	    response = self.client.post(url, data, format="json")
	    self.assertEqual(
	        response.status_code,
	        status.HTTP_401_UNAUTHORIZED
	    )