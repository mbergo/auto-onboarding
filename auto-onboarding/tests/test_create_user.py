import unittest
from selenium import webdriver

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/create_user/")

    def test_create_user(self):
        # Find form elements and input test data
        name = self.driver.find_element_by_name("name")
        email = self.driver.find_element_by_name("email")
        password = self.driver.find_element_by_name("password")
        submit = self.driver.find_element_by_xpath("//input[@type='submit']")

        # Input data
        name.send_keys("testuser")
        email.send_keys("testuser@example.com")
        password.send_keys("testpassword")

        # Submit form
        submit.click()

        # Check that the user was created successfully
        success_message = self.driver.find_element_by_xpath("//div[@class='response']").text
        self.assertEqual(success_message, "User created successfully")

    def tearDown(self):
        self.driver.close()

