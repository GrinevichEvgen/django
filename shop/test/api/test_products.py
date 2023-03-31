import product
import pytest
from rest_framework.test import APIClient

from products.models import Product
@pytest.mark.django_db
class TestProductsApi:
    def setup_method(self):
        self.client = APIClient()

    def test_index(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert len(response.json()) == 0

        response = self.client.post("/api/products/", data={
            "title": "Nokia3310",
            "color": "Red",
            "price": 100,
        })
        assert response.status_code == 201
        assert Product.objects.exists()

    def test_delete_product(self):
        product = Product.objects.create(title="Nokia 3310", color="Red", price=100)

        response = self.client.get(f"/api/products/{product.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "Nokia 3310"

        response = self.client.delete(f"/api/products/{product.id}/")
        assert response.status_code == 204
        assert not Product.objects.exists()

