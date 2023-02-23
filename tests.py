from flask import requests
import json
import unittest

class APITestCase(unittest.TestCase):
    
    def test_classify_image(self):
        url = "http://localhost:5000/classify"
        # Load test image
        with open("test_image.jpg", "rb") as f:
            image_data = f.read()
        # Create a multipart/form-data request with the test image
        files = {'image': ('test_image.jpg', image_data, 'image/jpeg')}
        response = requests.post(url, files=files)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn(data['class'], ['class_1', 'class_2', 'class_3'])

if __name__ == '__main__':
    unittest.main()
