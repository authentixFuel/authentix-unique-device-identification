import unittest
import os
from device_identification.device_storage import DeviceStorage

class TestDeviceStorage(unittest.TestCase):
    def setUp(self):
        self.storage_path = 'test_device_storage.json'
        self.device_storage = DeviceStorage(self.storage_path)

    def tearDown(self):
        if os.path.exists(self.storage_path):
            os.remove(self.storage_path)

    def test_add_device(self):
        user_id = 'user123'
        device_id = 'device456'
        self.device_storage.add_device(user_id, device_id)
        self.assertTrue(self.device_storage.is_device_registered(user_id, device_id))

    def test_is_device_registered(self):
        user_id = 'user123'
        device_id = 'device456'
        self.device_storage.add_device(user_id, device_id)
        self.assertTrue(self.device_storage.is_device_registered(user_id, device_id))
        self.assertFalse(self.device_storage.is_device_registered(user_id, 'nonexistent_device'))

if __name__ == '__main__':
    unittest.main()
