from django.test import SimpleTestCase


class AppTests(SimpleTestCase):
    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/characters/")

    def test_list(self):
        response = self.client.get("/characters/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["data"][0],
            {"id": 1, "name": "Rick Sanchez", "age": 70},
        )

    def test_detail(self):
        response = self.client.get("/characters/1/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["data"],
            {"id": 1, "name": "Rick Sanchez", "age": 70},
        )
