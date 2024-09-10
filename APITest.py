import requests
import unittest

class TestGetUserProfile(unittest.TestCase):

    def setUp(self):
        self.existing_user_url = "https://reqres.in/api/users/12"
        self.non_existing_user_url = "https://reqres.in/api/users/888"

    def test_get_user_profile_success(self):
        response = requests.get(self.existing_user_url)
        self.assertEqual(response.status_code, 200, "Status Must Be 200")
        data = response.json()

        # Request Body
        expected_user_data = {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }

        self.assertEqual(data['data'], expected_user_data, "User Profile Info Not Match")
        print(f"Status Code for existing user: {response.status_code}")
        print(f"Response Text for existing user: {response.text}")

    def test_get_user_profile_not_found(self):
        response = requests.get(self.non_existing_user_url)
        self.assertEqual(response.status_code, 404, "Status Must Be 404")
        self.assertEqual(response.text, "{}", "Infomation is null")
        print(f"Status Code for non-existing user: {response.status_code}")
        print(f"Response Text for non-existing user: {response.text}")

if __name__ == "__main__":
    unittest.main()