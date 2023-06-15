from locust import HttpUser, task


class MobileAppUser(HttpUser):
    token = None

    def on_start(self):
        data = {"email": "test@test.com", "password": "password"}
        response = self.client.post("/api/login/", data=data)
        self.token = response.json()["token"]


@property
def headers(self):
    return {"Authorization": f"Token {self.token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36"}


@task(weight=1)
def pages(self):
    self.client.get("/api/products/", headers=self.headers)
    self.client.get("/api/products/?min_cost=50", headers=self.headers)
    self.client.get("/api/purchases/", headers=self.headers)
